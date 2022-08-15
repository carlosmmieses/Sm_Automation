"""
    Creado: 20220730

    Script para automatizar los procesos de like,
    follow y comment a otras cuentas de Facebook, 
    Instagram y Twitter.

    '''
   Automatizacion de Instagram. Handles autenticacion. 
   Este script lo hice usando https://www.youtube.com/watch?v=c8i4CaELPME
   para autenticacion de fb y ig api y.

   Utilice este recurso https://www.youtube.com/watch?v=Q5kw7vGLqgs&t=1993s 
   para subir post a instagram de manera automatica.

   
   Requirements:
    1.Facebook business page
    2.Facebook graph api app
    3.Instagram permissions

   Pasos de configuracion: [no del algoritmo]
    1.Crear un cuenta de negocio o influencer en IG.
    2.Tener una pagina de negocio en FB.
    3.Conectar las cuentas.
    4.Crear un app de FB Graph API. 

   Permisos para publicar en paginas de Facebook:
    1.pages_manage_posts
    2.pages_read_engagement

   Permisos para instagram:
    publish_video
    pages_show_list
    instagram_basic
    instagram_manage_comments
    instagram_manage_insights
    instagram_content_publish
    instagram_manage_messages
    pages_read_engagement
    pages_read_user_content


    Cuenta: Finsoftpr

    NOTA: para subir contenido tiene que ser una cuenta business. 2022 07 30

    Este es el link de facebook.dev para los long-lived y short-lived tokens
    developers.facebook.com/docs/pages/access-tokens

'''


"""
#IMPORTACION DE MODULOS
#------------------------------------------------
from email import message
from email.utils import quote
from turtle import pos
from urllib import response
import requests
import json
import datetime as dt
import facebook as fb
import random
import schedule
import time
from uuid import uuid4
#------------------------------------------------


#CREDENCIALES DE GRAPH API DE FINSOFTPR
#------------------------------------------------
def getCreds():
    '''
        Diccionario donde voy a guardar toda la info de los
        creds que pide fb para usarlo para.
    '''
    creds = dict()
    creds['access_token'] = 'EAAXKEKee6M8BAO4zRKxj3ouii10aoXRpyIqBTpqZBfuZA2A7rUC686yoL2K4ihVqQbZCoaXJ24ZAuEg3tFptaZAXwZAcRZAZAcaCusKoRFyeSHp7Gj4SpBpX6wdYt8NVJbQtPl4LOuKebcjZA7yG08iWPKpaQgLd7HI0QZBnzxav4YPQZDZD'#expires: inmortal token
    creds['page_token'] = 'EAAXKEKee6M8BABpotbnQKQcQ2k4MbsYmr8ZCokHOVtfKZAG3djZBmCZAlZA1dZBpvXdcMQ66BYZBraw55wzlNssqkr6XZBbpQ4JQYeALeY8ovy3AGZA1bLF5UFmIaRqhgimUAZAWZAWRyftHThmPMvfXfNThSZC3yTurg8WLmYztdx0y83TTg0wj3a6S'#token de la pagina de facebook de Finsoftpr.
    creds['client_id'] = '1629547764050127' #El id del app que cree con FB.dev Finsoft Marketing
    creds['client_secret'] = 'c6e09932f59139d3c4e15b9078ccc875'
    creds['fb_page_id'] = '110476234837870' #id de la pagina de facebook de FinSoftpr
    creds['graph_domain'] = 'https://graph.facebook.com/' #root domain de Facebook Api.
    creds['graph_version'] = 'v14.0' #version del api.
    creds['endpoint_base'] = creds['graph_domain'] + creds['graph_version'] + '/' #root domain de donde se hacen los requests.
    creds['debug'] = 'no' # valor default es no, para hacer debug cambiar en el driver code.
    return creds
#------------------------------------------------

#FUNCION PARA CONECTAR EL API CON LOS CREDENCIALES
#------------------------------------------------
def makeApiCall(url, endpointParams, debug ='no'):
    '''
        Hace un get request al endpoint que se creo en def get_creds.

    ''' 
    data = requests.get(url, endpointParams) #http request
    response = dict() #diccionario para mostrar informacion del request
    response['url'] = url #url
    response['endpoint_params'] = endpointParams
    response['endpoint_params_pretty'] = json.dumps(endpointParams, indent=4) #for debugging.
    response['json_data'] = json.loads(data.content) # ver la data que recibo del endpoint.
    response['json_data_pretty'] = json.dumps(response['json_data'], indent=4) #save la data

    '''
        debug == yes le va a enseñar la data 
        del call.
    '''
    if ('yes' == debug):
        displayApiCallData(response)

    return response 
#------------------------------------------------

#FUNCION PARA MOSTRAR DATA DEL ACCESS TOKEN
#------------------------------------------------
def displayApiCallData(response):
    '''
        display de la data cuando hago un api call para debug.
    '''
    print("\nURL: ")
    print(response['url'])
    print("\nEndpoint Params: ")
    print(response['endpoint_params_pretty'])
    print("\nRespons")
    print(response['json_data_pretty'])
#------------------------------------------------

#------------------------------------------------
def debugAccessToken(params):
    '''
        Info sobre el access token.
        
        API endpoints: 
        https://graph.facebook.com/
        debug_token?input_token={input_token}&access_token={valid-access-token}

        Returns:
        Object: data from the endpoint
    '''
    endpointParams = dict()
    endpointParams['input_token'] = params['access_token']
    endpointParams['access_token'] = params['access_token']

    url = params['graph_domain'] + '/debug_token'

    return makeApiCall(url, endpointParams, params['debug'] )
#------------------------------------------------

#------------------------------------------------
def getLongLivedAccessToken(params):
    '''
       usa los creds para hacer un call para extender el uso del api.  
    '''
    endpointParams = dict()
    endpointParams['grant_type'] = 'fb_exchange_token'
    endpointParams['client_id'] = params['client_id']
    endpointParams['client_secret'] = params['client_secret']
    endpointParams['fb_exchange_token'] = params['access_token']

    url = params['endpoint_base'] + 'oauth/access_token'
    return makeApiCall(url, endpointParams, params['debug'])  
#------------------------------------------------

#------------------------------------------------
#POST QUOTES EN FACEBOOK
'''

    ESTA SECCION ES PARA SUBIR CONTENIDO A FACEBOOK

    La documentacion para subir contenido a Facebook esta en este
    link: https://developers.facebook.com/docs/pages/publishing

    Perminso para subir contenido a Facebook.
        1.page_manage_post
        2.page_read_engagement
        3.publish_to_grups

'''
def postFbQuote(access_token, mensaje):
    user = fb.GraphAPI(access_token)
    user.put_object('me', 'feed', message=mensaje)
#------------------------------------------------


#------------------------------------------------
#FUNCION PARA SUBIR IMAGENES A FACEBOOK
fbcounter = 0
def postFbImage():
    blog_url = 'https://finsoftpr.com/blog'
    base_url = 'https://finsoftpr.com'
    services_url = 'https://finsoftpr.com/servicios'
    about_url = 'https://finsoftpr.com/'
    # ---- Lista de captions --------------------------
    msg_list = [
        'En finsoftpr queremos lo mejor para nuestros clientes, visita nuestro blog en ' + blog_url,
        'Que esperas para visitar nuestro website! ' + base_url,
        'Explora nuestros servicios ' + services_url,
        'Somo una empresa 100% local dedicada nuestros clientes ' + base_url,
        'Explora que nos hace diferente ' + about_url,
        'Hacemos posible lo imposible ' + services_url,
    ]
    # -------------------------------------------------

    #---HASHTAGS----------------------------------------
    hashtags = '#Finsoftpr #webdesign #automatizacion #smallbusiness #webmanagement #wordpress #webdesignpr #pr'
    #---------------------------------------------------
    # --- Caption random ------------------------------
    caption = random.choice(msg_list) + hashtags
    #--------------------------------------------------
    page_token = 'EAAXKEKee6M8BABpotbnQKQcQ2k4MbsYmr8ZCokHOVtfKZAG3djZBmCZAlZA1dZBpvXdcMQ66BYZBraw55wzlNssqkr6XZBbpQ4JQYeALeY8ovy3AGZA1bLF5UFmIaRqhgimUAZAWZAWRyftHThmPMvfXfNThSZC3yTurg8WLmYztdx0y83TTg0wj3a6S'#page token de FinSoftpr
    n = random.randint(1,23) #para postear fotos random
    postFbImage.counter += 1
    img_url = f'https://i0.wp.com/finsoftpr.com/wp-content/uploads/2022/08/{postFbImage.counter}.png?fit=1414%2C2000&ssl=1'
    
    fb_page_id = '110476234837870' #Id de la pagina de Finsoftpr en Facebook.
    post_img_url = 'https://graph.facebook.com/{}/photos'.format(fb_page_id)
    img_payload = {
        'message': caption,
        'url': img_url,
        'access_token': page_token,
    }
    r = requests.post(post_img_url, data=img_payload)
    print(r.text)
postFbImage.counter = fbcounter
#------------------------------------------------

#------------------------------------------------
#FUNCION PARA SUBIR UNA IMAGEN A INSTAGRAM
igcounter = 0
def postIgImage():
    blog_url = 'https://finsoftpr.com/blog'
    base_url = 'https://finsoftpr.com'
    services_url = 'https://finsoftpr.com/servicios'
    about_url = 'https://finsoftpr.com/'

    msg_list = [
        'En finsoftpr queremos lo mejor para nuestros clientes, visita nuestro blog en ' + blog_url,
        'Que esperas para visitar nuestro website! ' + base_url,
        'Explora nuestros servicios ' + services_url,
        'Somo una empresa 100% local dedicada nuestros clientes' + base_url,
        'Explora que nos hace diferente' + about_url,
    ]
    #---HASHTAGS----------------------------------------
    hashtags = '#Finsoftpr #webdesign #automatizacion #smallbusiness #webmanagement #wordpress #webdesignpr #pr'
    #---------------------------------------------------
    caption = random.choice(msg_list) +  "  " + hashtags
    
    page_token = 'EAAXKEKee6M8BABpotbnQKQcQ2k4MbsYmr8ZCokHOVtfKZAG3djZBmCZAlZA1dZBpvXdcMQ66BYZBraw55wzlNssqkr6XZBbpQ4JQYeALeY8ovy3AGZA1bLF5UFmIaRqhgimUAZAWZAWRyftHThmPMvfXfNThSZC3yTurg8WLmYztdx0y83TTg0wj3a6S'#page token de FinSoftpr
    n = random.randint(1,23) #para postear fotos random
    postIgImage.counter += 1
    img_url = f'https://i0.wp.com/finsoftpr.com/wp-content/uploads/2022/08/{postFbImage.counter}.png?fit=1414%2C2000&ssl=1'
  
    '''
        Recordatorio: IG solo acepta fotos formato .jpeg
    '''
    ig_page_id = '17841449992944042' #id de la pagina de Finsoftpr business IG.
    #Post the Image..................................................................
    '''
        Este es el primer paso para POST una foto a instagram.
        En este paso se va a crear el image_creation_id para 
        que instagram este seguro que el formato es el adecuado.

        Para que IG pueda importar mis imagenes, las imagenes tienen 
        que estar en un servidor publico.

    '''

    post_url = 'https://graph.facebook.com/v14.0/{}/media'.format(ig_page_id) #post_url de FB para autenticar el usuario de IG.

    payload = { #dic con los parametros que necesita el api de IG para POST.
        'image_url': img_url, #servidor publico donde yo hosteo mis templates.
        'caption': caption, #descripcion del post.
        'access_token': page_token
    }

    '''
        Modulo request hace un https request con el post url y concatena
        la data del dic payload y va a guardar el valor en la variable 
        resultado.
    '''
    r = requests.post(post_url, data=payload) 
    print(r.text)
    result = json.loads(r.text)
    '''
        Verifica si el dic result tiene el key 'id' para usarlo como
        creation id del API de IG, si esta guardar ese id 
        en la variable creation_id.

    '''
    if 'id' in result:
        creation_id = result['id']

        second_url = 'https://graph.facebook.com/v14.0/{}/media_publish'.format(ig_page_id)
        second_payload = {
            'creation_id': creation_id,
            'access_token': page_token
        }

    
        '''
        Este es el segundo paso para POST una foto a instagram.
        En este paso se va usar la variable creation_id para 
        hacer el https request con el second_url y los valores del
        dic second_payload. 
        '''
        r = requests.post(second_url, data=second_payload)
        print('-------------Post It!!-------------------')
        print(r.text)
    else:
        print('oh-oh')
postFbImage.counter = igcounter
#------------------------------------------------

#---------------------------------------------------
#FUNCION QUE DEVUELVE UN MENSAJE RANDOM PARA POSTEAR 
def message_list():
    '''
        Esta funcion tiene una lista de quotes ya pre-hechos para devolver,
        un for loop para ir en devolviendo uno a uno cada vez que la funcion sea llamada.

        Para esta funcion corra como yo quiero tengo que tener el programa 24/7 corriendo
    '''
    blog_url = 'https://finsoftpr.com/blog'
    base_url = 'https://finsoftpr.com'
    services_url = 'https://finsoftpr.com/servicios'
    about_url = 'https://finsoftpr.com/'

    msg_list = [
        'En finsoftpr queremos lo mejor para nuestros clientes, visita nuestro blog en ' + blog_url,
        'Que esperas para visitar nuestro website! ' + base_url,
        'Explora nuestros servicios ' + services_url,
        'Somo una empresa 100% local dedicada nuestros clientes' + base_url,
        'Explora que nos hace diferente' + about_url,
    ]
    
    return random.choice(msg_list)
#---------------------------------------------------   

#---------------------------------------------------
#FUNCION PARA DEVOLVER UNA IMAGEN DISTINTA DE LA GALERIA
x = 0
def get_new_image():
    get_new_image.counter += 1
    img_url = f'https://i0.wp.com/finsoftpr.com/wp-content/uploads/2022/08/{get_new_image.counter}.png?fit=1414%2C2000&ssl=1'
    
    return img_url
get_new_image.counter = x
#---------------------------------------------------

#---------------------------------------------------
#FUNCION PARA CREAR IMAGENES CON CONTENIDO
def make_new_image():
    pass
#---------------------------------------------------

#FUNCION PARA CONSEGUIR LA LISTA DE FOLLOWERS
#---------------------------------------------------
def get_followers():
    pass
#---------------------------------------------------

#---HASHTAGS----------------------------------------
hashtags = '#Finsoftpr #webdesign #automatizacio #smallbusiness #webmanagement #wordpress'
#---------------------------------------------------


###################################################
#--------------------------------------------------
#----------------- DRIVER CODE --------------------------
#--------------------------------------------------
###################################################
'''
    Corre las funciones para autentificar, debug,
    mostrar y extender el access token de FB y IG.
'''
params = getCreds()
params['debug'] = 'no'
response = debugAccessToken(params)
#response = getLongLivedAccessToken(params)

if response == getLongLivedAccessToken(params):
    #Informacion sobre el longLive access token.
    print('---- ACESS TOKEN INFO ----')
    print('Access Token: ')
    print(response['json_data']['access_token'])
elif response == debugAccessToken(params):
   #Tener la info de cuando se vence el api.
   print('\nExpires at: ')
   print(dt.datetime.fromtimestamp(response['json_data']['data']['data_access_expires_at']))
else:
    pass

#---Post en FB -----------------------------------
mensaje = 'Estamos trabajando en la automatizacion de procesos {}'.format(hashtags)
access_token = params['page_token']
#post = postFbQuote(access_token, mensaje)
#----------------------------------------------

#---Publicar una foto en Facebook -----------------
msg = message_list()
mensaje = msg + hashtags
#imagen = schedule.every(1).minutes.do(get_new_image)
#postFbImage(access_token, imagen, mensaje)
#----------------------------------------------

#---Publicar una foto en Instagram ------------------
#access_token = params['page_token']
#imagen = 'https://i0.wp.com/finsoftpr.com/wp-content/uploads/2022/08/1.png?fit=1414%2C2000&ssl=1'
#postIgImage(access_token,imagen, mensaje)
#----------------------------------------------



#schedule.every(1).minutes.do(postFbImage)
#schedule.every(1).minutes.do(postIgImage)
while True:
 
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(10)
    #postFbImage(access_token, imag, mensaje)
    #postIgImage(access_token,imag, mensaje)

####################################################
#--------------------------------------------------
#----------------- END DRIVER CODE --------------------------
#--------------------------------------------------
##################################################### 