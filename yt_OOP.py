api_key = 'AIzaSyD0w7vp4wnt8D_RZJKddkNzuoRLHs4FV84'
api_version = 'v3'


import os
import re
import pickle
from datetime import timedelta
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


#Definicion de la clase Auth.
'''
    Clase base que se encarga de la autenticacion del usuario.
'''
class Auth:
    scopes = dict()
    scopes['upload'] = 'https://www.googleapis.com/auth/youtube.upload'
    scopes['readonly'] = 'https://www.googleapis.com/auth/youtube.readonly'
    scopes['ssl']=['https://www.googleapis.com/auth/youtube.force-ssl']

    def get_new_access_token(self):    
        credentials = None
            # token.pickle looks for a file called token.pstores the user's credentials from previously successful logins
        if os.path.exists('token.pickle'):
            print('Loading Credentials From File...')
            with open('token.pickle', 'rb') as token:
                credentials = pickle.load(token)

            # If there are no valid credentials available, then either refresh the token or log in.
        if not credentials or not credentials.valid:
            if credentials and credentials.expired and credentials.refresh_token:
                print('Refreshing Access Token...')
                credentials.refresh(Request())
            else:
                print('Fetching New Tokens...')
                flow = InstalledAppFlow.from_client_secrets_file(
                    'client_secrets.json',
                    scopes=[scopes['readonly'], scopes['upload']]
                )
                flow.run_local_server(port=8080, prompt='consent',
                            authorization_prompt_message='')
                credentials = flow.credentials

                # Save the credentials for the next run
        with open('token.pickle', 'wb') as f:
            print('Saving Credentials for Future Use...')
            pickle.dump(credentials, f)  
        return credentials    


x = Auth

print(x)