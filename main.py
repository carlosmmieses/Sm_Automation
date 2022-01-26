'''
    En este modulo voy a combinar todas las funciones del programa
    para que corran de manera sincronizada.

    El modulo permite que el usuario cree y postee manualmente y de
    manera automatica.
    
    TODO:
        1.DONE Set up el vps para  que el programa corra 24/7.
        2.Combinar las tres funciones al main.py para que se sincronicen
        3.Conseguir templates para luego añadirle foto de los carros.
        4.Crear app gui para que usuarios/empleados puedan subir su contenido.
'''
from ig_automation import postIgImage
from fb_automation import postFbQuote, postFbImage
from sm_authentication import get_MetaCreds
import schedule
import time
import sys
'''
Credenciales para las plataformas de Meta(Facebook e Instagram).
'''
creds = get_MetaCreds()
#print(creds['access_token'])


mm_creds = dict()
mm_creds['inmortal_token'] = 'EAAOY45w3TmwBAKSZA2QPVeOJBAqJkSzNDlVpsrIDTHrFV6WRRJ1jFdZAnHDetZCO8DXUVN9lpJbD0XKwYxdTc21GFYwixHyeUoIWZAmHub4zQVWyp9OyhDR0mqckkOPUbitquZBak4sWPGGQIAZB5wZAAyLZAXEVGR6xlJWsqBFgLyVrZCZBGZA6ZClA'


#postcreation no puede tener ningun para
def postcreation():
    quote = "Ram 1500 Laramie 2019 llama para inf 787-530-2594"
    img_name = 'ram'
    img_file = 'https://finsoftmarketing.fra1.digitaloceanspaces.com/{}'.format(img_name)
    creds = get_MetaCreds()
    #print(creds['access_token'])
    
    postFbImage(creds['access_token'], img_file, quote)
    postIgImage(img_name, quote)


post_time = '10:02'
def debug():
    print('test')

# def ManualPost():
    
#     schedule.every().wednesday.at('12:48').do(debug)
    #FALTA INSTAGRAM SETEO PARA MEJIMOTORS#igpost = postIgImage(img_file, quote)
    
    
'''
    Modulo schedule para fijar fecha y hora en la cual se va POST.
'''
#schedule.every().monday.at('13:36').do(postInstagramQuote) #definicion de instruccion.
#schedule.every().monday.at('13:36').do(postFbQuote)
#ManualPost()

# debug
# schedule.every().wednesday.at('12:48').do(debug)
#schedule.every().wednesday.at(post_time).do(debug)
schedule.every().wednesday.at(post_time).do(postcreation)
while True:
    schedule.run_pending() #metodo para correr la cantindad  schedules que tenga.
    time.sleep(1)