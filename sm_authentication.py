'''
    En este modulo esta la configuracion de autenticacion de Meta, Twitter
    y Youtube.
'''

def get_MetaCreds():
    '''
        Diccionario donde voy a guardar toda la info de los
        creds que pide Meta para usarlo.
    '''
    creds = dict()
    creds['access_token'] = 'EAAFzr8vnjJoBAGLWHykFZB94ZCQRtsQRulpd7ZBZAd8SwLlfHHZBY7vJWr6ix3mdN90MCHuW4WMirpVvURYdCEMVvbFq1bSGzyj1vK2VlnA9fQGWijilvk9HuCkg0p3N4vpb1MesBkmHqjwByerZBltZC3Qp5ZCZAUFkiFrPegZCNyL5MZAWWTD3ZBsKULW4HF767twZD' #expires: inmortal token
    creds['client_id'] = '408673854131354' #El id del app que cree con FB.dev
    creds['client_secret'] = '2606f3cb1d1337c9420cdc60e528c467'
    creds['graph_domain'] = 'https://graph.facebook.com/' #root domain de Facebook Api.
    creds['graph_version'] = 'v12.0' #version del api.
    creds['endpoint_base'] = creds['graph_domain'] + creds['graph_version'] + '/' #root domain de donde se hacen los requests.
    creds['fb_page_id'] = '110476234837870'
    creds['ig_page_id'] = '17841449992944042'
    creds['debug'] = 'no' #
    return creds


import facebook as fb
#page_token = 'EAAFzr8vnjJoBAAlLPyq0jjoppCNE3IWSDHvYWdBZCWpQcKi0TA6iKOshVLJU4dmLXnmzZBZCV8GV3CuDpjDvfKhaawSSCzJpRfoEtwOXVB0hLwQi21hIW8mXr3vRPEJikigvmZAu4BjGtRlSVcTZA7G7lRknrDWU0Nk2FhbMDL4kqKnDmZCq0TZBAYE9BZAZAxrEZD'

#this is facebook manage page token.
inmortal_token = 'EAAFzr8vnjJoBAHy6Y1TeM9VINoTBq6R9gdNhkzQT9vp1kePVXZA39ngZACypGYYJILkZA0XoZBByvZAcd2bi3vTeCPKZBI9sXnJjzxZBAcupNeH5nOtT0HTFG7ffcLnB6zeuZAjqbfwuWZABdAbovfuBx0IrAJvQkOmFUJGs2R7ZCczQfHhCdgUuyMfxxCrqmPRgEZD'
inmortal_tk_id = '110476234837870'
ig_id = '17841449992944042'
fb_page_id = '110476234837870'
# user = fb.GraphAPI(page_token)
# user.put_object('me','feed',message='This is an automated post!!:)')