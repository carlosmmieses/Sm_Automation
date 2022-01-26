"""
Script que  autentifica y crea un post.

BUGS:
    las variable de fb_pageid y acces_token tienen que ser una sola
    todo el programa porque se me olvida cambiarla.

"""
from email import message
import facebook as fb
#page_token = 'EAAFzr8vnjJoBAAlLPyq0jjoppCNE3IWSDHvYWdBZCWpQcKi0TA6iKOshVLJU4dmLXnmzZBZCV8GV3CuDpjDvfKhaawSSCzJpRfoEtwOXVB0hLwQi21hIW8mXr3vRPEJikigvmZAu4BjGtRlSVcTZA7G7lRknrDWU0Nk2FhbMDL4kqKnDmZCq0TZBAYE9BZAZAxrEZD'

#this is facebook manage page token.
inmortal_token = 'EAAFzr8vnjJoBAHy6Y1TeM9VINoTBq6R9gdNhkzQT9vp1kePVXZA39ngZACypGYYJILkZA0XoZBByvZAcd2bi3vTeCPKZBI9sXnJjzxZBAcupNeH5nOtT0HTFG7ffcLnB6zeuZAjqbfwuWZABdAbovfuBx0IrAJvQkOmFUJGs2R7ZCczQfHhCdgUuyMfxxCrqmPRgEZD'
inmorta_tk_id = '110476234837870'
ig_id = '17841449992944042'
fb_page_id = '110476234837870'

mm_fb_pageid = '100113478125472'
# user = fb.GraphAPI(page_token)
'''
    los parametros son: me=quien esta haciendo la publicacion,
    feed=en donde lo voy a postear, 
    message= el mensaje que quiero postear.
'''
# user.put_object('me','feed',message='This is an automated post!!:)')

def postFbQuote():
    user = fb.GraphAPI(inmortal_token)
    user.put_object('me', 'feed', message='Just a few more days for launch!!')
#########################################################################
#########################################################################


'''
    Esta parte de abajo del script es correspondiente al tutorial
    de skolo Online.
    Este tutorial me dara contexto para trabajar con el de instagram.

'''

import requests
import random


msg = 'Hi! I am getting ready for deployment!!'
app_secret = '2606f3cb1d1337c9420cdc60e528c467'
descripciones = [
    'descripcion #1',
    'descripcion #2',
    'descripcion #3',
    'descripcion #4',
    'descripcion #5',
    'descripcion #6'
]
#Publish a post.
# post_url = 'https://graph.facebook.com/{}/feed'.format(fb_page_id)
# payload = {
#     'message': msg,
#     'acces_token': page_token
# }

#r = requests.post(post_url, data=payload)

#Publish a photo.
def postFbImage(page_token, img_file, message):
    img_url = 'https://finsoftmarketing.fra1.digitaloceanspaces.com/{}.jpeg'.format(img_file)
    post_img_url = 'https://graph.facebook.com/{}/photos'.format(fb_page_id)
    img_payload = {
        'message': message,
        'url': img_url,
        'access_token': page_token,
    }
    r = requests.post(post_img_url, data=img_payload)
    print(r.text)


#postFbImage(inmortal_token, 'ram', msg)