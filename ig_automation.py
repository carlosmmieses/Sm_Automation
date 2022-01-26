
from email.utils import quote
import requests
import json
import datetime as dt
'''
   Automatizacion de Instagram. Handles autenticacion. 
   Este script lo hice usando https://www.youtube.com/watch?v=c8i4CaELPME
   para autenticacion de fb y ig api y.

   Utilice este recurso https://www.youtube.com/watch?v=Q5kw7vGLqgs&t=1993s 
   para subir post a instagram de manera automatica.


   Requirements:
    1.Facebook app

'''



def getCreds():
    '''
        Diccionario donde voy a guardar toda la info de los
        creds que pide fb para usarlo para.
    '''
    creds = dict()
    creds['access_token'] = 'EAAFzr8vnjJoBAGLWHykFZB94ZCQRtsQRulpd7ZBZAd8SwLlfHHZBY7vJWr6ix3mdN90MCHuW4WMirpVvURYdCEMVvbFq1bSGzyj1vK2VlnA9fQGWijilvk9HuCkg0p3N4vpb1MesBkmHqjwByerZBltZC3Qp5ZCZAUFkiFrPegZCNyL5MZAWWTD3ZBsKULW4HF767twZD' #expires: inmortal token
    creds['client_id'] = '408673854131354' #El id del app que cree con FB.dev
    creds['client_secret'] = '2606f3cb1d1337c9420cdc60e528c467'
    creds['graph_domain'] = 'https://graph.facebook.com/' #root domain de Facebook Api.
    creds['graph_version'] = 'v12.0' #version del api.
    creds['endpoint_base'] = creds['graph_domain'] + creds['graph_version'] + '/' #root domain de donde se hacen los requests.
    creds['debug'] = 'no' #
    return creds


def makeApiCall(url, endpointParams, debug ='no'):
    '''
        Hace un get request al endpoint que se creo en def get_creds.

    ''' 
    data = requests.get(url, endpointParams) #httpp request
    response = dict()
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


def debugAccessToken(params):
    '''
        Info sobre el access token.
    '''
    endpointParams = dict()
    endpointParams['input_token'] = params['access_token']
    endpointParams['access_token'] = params['access_token']

    url = params['graph_domain'] + '/debug_token'

    return makeApiCall(url, endpointParams, params['debug'] )


def getLongLivedAccessToken(params):
    '''
       usa los creds para hacer un call para extender el uso del api.

       nota: esa funcion no me esta funcionando. 20220110  
    '''
    endpointParams = dict()
    endpointParams['grant_type'] = 'fb_exchange_token'
    endpointParams['client_id'] = params['client_id']
    endpointParams['client_secret'] = params['client_secret']

    url = params['endpoint_base'] + 'oauth/access_token'
    return makeApiCall(url, endpointParams, params['debug'])    

# #Driver code para accesso al api. [first resource]
# params = getCreds()
# params['debug'] = 'yes'
# response = debugAccessToken(params)

#Tener la info de cuando se vence el api.
# print('\nExpires at: ')
# print(dt.datetime.fromtimestamp(response['json_data']['data']['data_access_expires_at']))

#Info sobre el longLive access token.
# print('---- ACESS TOKEN INFO ----')
# print('Access Token: ')
# print(response['json_data']['access_token'])


'''
    ESTA SECCION ES PARA SUBIR CONTENIDO A INSTAGRAM.
    2022 01 12 -- Hoy voy a hacer los websites de wordpress. 
                    mañana 2022 01 13 voy a seguir con FinSoft
                    Automation. Me quede en 1;17;32

    TODO:
    1.create a vps to host images.
    2.request a content object container id from the Graph Api. 
    De este momento en adelante voy a interactuar con el segundo recurso.

    Para que el script funcione 24/7 tengo que usar un vps

    requirements:
        requests 
        uuid4 - Crea un uuid(universal unique identifier) inmutable.
                Esto va a crear nombres unicos para los templates
        
        random - Devuelve un valor 'aleatorio' dentro de una lista o file.
        
        json - Permite a python leer json files.
        
        schedule - Python job shceduling for human. Run Python functions
        (or any other callable) periodically using a friendly syntax.
    
        time -  Time related function.  Esto va a darle tiempo para que la
                logica pueda funcionar.

        
'''
import requests
import random
import json
import schedule
import time
from uuid import uuid4
#from .template_creation import createQuoteImg, quote_images

creds = getCreds()
fb_page_id = '110476234837870'
ig_page_id = '17841449992944042'
'''
    def get_igbusiness_id. 
    funcion para obtener el id de la pagina de ig.
    parametros: 
        facebook page id
        instagram_business_account param
        access_token
    return instagram_business_account
'''
def postIgImage(img_name, caption):
    #image_name = 'ram' #'image-'+str(uuid4()).split('-')[4] #Crea un nombre unico para cada imagen.
  
    '''
        Recordatorio: IG solo acepta fotos formato .jpeg
    '''
    image_location = 'https://finsoftmarketing.fra1.digitaloceanspaces.com/{}.jpeg'.format(img_name)#'path/to/image/{}'.fomat(image_name) #lugar en el servidor donde estan almacenadas las fotos.

    #Create the Image .............
    filename = 'https://finsoftmarketing.fra1.digitaloceanspaces.com/' #lugar en el servidor donde estan las imagenes.
    quotes = ''#readJson(filename) #abre el file donde estan los quotes.
    #quote = 'Ram 1500 Laramie 2019 llama para inf 787-530-2594'#random.choice(quotes) #escoge un quote random.

    '''
        Instanciando la funcion del template_creation con los attributos
        del random quote definido enla linea 161, el background image del
        template_creation 
    '''
    #createQuoteImg(quote, quote_images, image_location)
  
    #wait for one second
    time.sleep(3)

    #Post the Image..................................................................
    '''
        Este es el primer paso para POST una foto a instagram.
        En este paso se va a crear el image_creation_id para 
        que instagram este seguro que el formato es el adecuado.

        Para que IG pueda importar mis imagenes, las imagenes tienen 
        que estar en un servidor publico.

    '''
    image_location_1 = image_location#'https://image...' #lugar en el servidor publico donde estan los templates guardados.
    post_url = 'https://graph.facebook.com/v12.0/{}/media'.format(ig_page_id) #post_url de FB para autenticar el usuario de IG.

    payload = { #dic con los parametros que necesita el api de IG para POST.
        'image_url': image_location_1, #servidor publico donde yo hosteo mis templates.
        'caption': caption, #descripcion del post.
        'access_token': creds['access_token']
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

        second_url = 'https://graph.facebook.com/v12.0/{}/media_publish'.format(ig_page_id)
        second_payload = {
            'creation_id': creation_id,
            'access_token': creds['access_token']
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


'''
    Esta parte del script es donde voy hacer el schedule para poder
    subir el el contenido de manera cronologica.
    Esta parte deberia estar en el main file con los schedule de las 
    otras redes.

'''
#sample code:
# schedule.every().monday.at('08:10').do(postInstagramQuote) #definicion de instruccion.
# while True:
#     schedule.run_pending() #metodo para correr la cantindad  schedules que tenga.
#     time.sleep(1)


#DRIVER CODE:
#postInstagramQuote()



#########################--END OF CODE--############################

'''
    Limitaciones:
        hay un limite de 25 por 24hrs usando el api.
        Para poder escalar y tener mas cuentas necesito un proxy para 
        que ig no piense que lo estoy spameando.
    
'''
