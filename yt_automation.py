#########################################################################
### Creador: Carlos Andres Mejias Mieses                              ###
### Fecha: 2021 12 27                                                 ###
### Proposito: Crear un script que automatice CRUD.                   ###
###                                                                   ###
###                                                                   ###
###                                                                   ###
#######################################################################

#TODO: Cambiar el diseño a OOP y automatizar upload.


api_key = 'AIzaSyD0w7vp4wnt8D_RZJKddkNzuoRLHs4FV84'
api_version = 'v3'


import os
import re
import pickle
from datetime import timedelta
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

#credentials = None
scopes = dict()
scopes['upload'] = 'https://www.googleapis.com/auth/youtube.upload'
scopes['readonly'] = 'https://www.googleapis.com/auth/youtube.readonly'
scopes['ssl']=['https://www.googleapis.com/auth/youtube.force-ssl']



# #Definicion de objeto de autenticacion.
# flow = InstalledAppFlow.from_client_secrets_file('client_secrets.json', scopes=[scopes['readonly'], scopes['upload']])

# #run the local server.
# flow.run_local_server(port=8080, prompt='consent')

#credentials = flow.credentials

#def get_new_access_token():
#Fetch a new access token once it expires.
def get_new_access_token():
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


credentials = get_new_access_token()





def get_playlist_time(credentials):
  #Iniciacion del objeto de Youtube API.
  youtube = build('youtube', 'v3', credentials=credentials)

  #Regular expresions that parse the patterns that the 
  #API give back.
  hours_pattern = re.compile(r'(\d+)H') #Grab the digits before H.
  minutes_pattern = re.compile(r'(\d+)M') #Grab the digits before M.
  seconds_pattern = re.compile(r'(\d+)S') #Grab the digits before S.

  total_seconds = 0


  nextPageToken = None
  while True:
      #request para recibir los detalles de un playlist.
      pl_request = youtube.playlistItems().list(
          part='contentDetails',
          playlistId='PLEsfXFp6DpzRMby_cSoWTFw8zaMdTEXgL',#'PL0-84-yl1fUnRuXGFe_F7qSH1LEnn9LkW',#'PL0glhsZ01I-AsN7PRMNWH9X9XJKVpGSWJ',#'PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_',#"PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU",
          maxResults=50,
          pageToken=nextPageToken
      )
      #Guarda los resultados en dict
      pl_response = pl_request.execute()

      vid_ids = []
      for item in pl_response['items']: #busca el key items
          vid_ids.append(item['contentDetails']['videoId'])#por cada item añade el id del video y detalles.

      vid_request = youtube.videos().list(
          part="contentDetails",
          id=','.join(vid_ids)
      )

      vid_response = vid_request.execute()

      for item in vid_response['items']:
          duration = item['contentDetails']['duration'] #por cada item guardo la duracion de cada video.
          #Coge el string de duracion y lo distribuye en hora, minuto y segundo.
          hours = hours_pattern.search(duration)
          minutes = minutes_pattern.search(duration)
          seconds = seconds_pattern.search(duration)
          #Ternary expression que cambia de string a int para sumarlo y lo guarda en la variable hora.
          hours = int(hours.group(1)) if hours else 0  #if there is a value in hours group them, else give 0 as default.
          minutes = int(minutes.group(1)) if minutes else 0
          seconds = int(seconds.group(1)) if seconds else 0
          #Añade todas las hora, los minutos y segundos.
          video_seconds = timedelta(
              hours=hours,
              minutes=minutes,
              seconds=seconds
          ).total_seconds() 
          #Suma los segundo
          total_seconds += video_seconds
      #the nextPage token returns the value of the next video in the playlist.
      nextPageToken = pl_response.get('nextPageToken')
      #if there are no more videos in the playlist, break out of the loop.
      if not nextPageToken:
          break

  total_seconds = int(total_seconds)

  minutes, seconds = divmod(total_seconds, 60)
  hours, minutes = divmod(minutes, 60)

  print(f'{hours}:{minutes}:{seconds}')

get_playlist_time(credentials)



# def upload_video(credentials):
#      #Iniciacion del objeto de Youtube API.
#   youtube = build('youtube', 'v3', credentials=credentials)

# def upload_video():
#   # token.pickle stores the user's credentials from previously successful logins
#   if os.path.exists('token.pickle'):
#       print('Loading Credentials From File...')
#       with open('token.pickle', 'rb') as token:
#           credentials = pickle.load(token)




#   # If there are no valid credentials available, then either refresh the token or log in.
#   if not credentials or not credentials.valid:
#       if credentials and credentials.expired and credentials.refresh_token:
#           print('Refreshing Access Token...')
#           credentials.refresh(Request())
#       else:
#           print('Fetching New Tokens...')
#           flow = InstalledAppFlow.from_client_secrets_file(
#               'client_secrets.json',
#               scopes=[
#                   'https://www.googleapis.com/auth/youtube.readonly'
#               ]
#           )

#           flow.run_local_server(port=8080, prompt='consent',
#                                 authorization_prompt_message='')
#           credentials = flow.credentials

#           # Save the credentials for the next run
#           with open('token.pickle', 'wb') as f:
#               print('Saving Credentials for Future Use...')
#               pickle.dump(credentials, f)  

















































# import argparse
# import httplib2
# import os
# import random
# import time

# import google.oauth2.credentials
# import google_auth_oauthlib.flow
# from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError
# from googleapiclient.http import MediaFileUpload
# from google_auth_oauthlib.flow import InstalledAppFlow


# # Explicitly tell the underlying HTTP transport library not to retry, since
# # we are handling retry logic ourselves.
# httplib2.RETRIES = 1

# # Maximum number of times to retry before giving up.
# MAX_RETRIES = 10

# # Always retry when these exceptions are raised.
# RETRIABLE_EXCEPTIONS = (httplib2.HttpLib2Error, IOError, httplib.NotConnected,
#   httplib.IncompleteRead, httplib.ImproperConnectionState,
#   httplib.CannotSendRequest, httplib.CannotSendHeader,
#   httplib.ResponseNotReady, httplib.BadStatusLine)

# # Always retry when an apiclient.errors.HttpError with one of these status
# # codes is raised.
# RETRIABLE_STATUS_CODES = [500, 502, 503, 504]

# # The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# # the OAuth 2.0 information for this application, including its client_id and
# # client_secret. You can acquire an OAuth 2.0 client ID and client secret from
# # the {{ Google Cloud Console }} at
# # {{ https://cloud.google.com/console }}.
# # Please ensure that you have enabled the YouTube Data API for your project.
# # For more information about using OAuth2 to access the YouTube Data API, see:
# #   https://developers.google.com/youtube/v3/guides/authentication
# # For more information about the client_secrets.json file format, see:
# #   https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
# CLIENT_SECRETS_FILE = 'client_secret.json'

# # This OAuth 2.0 access scope allows an application to upload files to the
# # authenticated user's YouTube channel, but doesn't allow other types of access.
# SCOPES = ['https://www.googleapis.com/auth/youtube.upload']
# API_SERVICE_NAME = 'youtube'
# API_VERSION = 'v3'

# VALID_PRIVACY_STATUSES = ('public', 'private', 'unlisted')


# # Authorize the request and store authorization credentials.
# def get_authenticated_service():
#   flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
#   credentials = flow.run_console()
#   return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)

# def initialize_upload(youtube, options):
#   tags = None
#   if options.keywords:
#     tags = options.keywords.split(',')

#   body=dict(
#     snippet=dict(
#       title=options.title,
#       description=options.description,
#       tags=tags,
#       categoryId=options.category
#     ),
#     status=dict(
#       privacyStatus=options.privacyStatus
#     )
#   )

#   # Call the API's videos.insert method to create and upload the video.
#   insert_request = youtube.videos().insert(
#     part=','.join(body.keys()),
#     body=body,
#     # The chunksize parameter specifies the size of each chunk of data, in
#     # bytes, that will be uploaded at a time. Set a higher value for
#     # reliable connections as fewer chunks lead to faster uploads. Set a lower
#     # value for better recovery on less reliable connections.
#     #
#     # Setting 'chunksize' equal to -1 in the code below means that the entire
#     # file will be uploaded in a single HTTP request. (If the upload fails,
#     # it will still be retried where it left off.) This is usually a best
#     # practice, but if you're using Python older than 2.6 or if you're
#     # running on App Engine, you should set the chunksize to something like
#     # 1024 * 1024 (1 megabyte).
#     media_body=MediaFileUpload(options.file, chunksize=-1, resumable=True)
#   )

#   resumable_upload(insert_request)

# # This method implements an exponential backoff strategy to resume a
# # failed upload.
# def resumable_upload(request):
#   response = None
#   error = None
#   retry = 0
#   while response is None:
#     try:
#       print('Uploading file...')
#       status, response = request.next_chunk()
#       if response is not None:
#         if 'id' in response:
#           print('Video id "%s" was successfully uploaded.') % response['id']
#         else:
#           exit('The upload failed with an unexpected response: %s' % response)
#     except HttpError, e:
#       if e.resp.status in RETRIABLE_STATUS_CODES:
#         error = 'A retriable HTTP error %d occurred:\n%s' % (e.resp.status,
#                                                              e.content)
#       else:
#         raise
#     except RETRIABLE_EXCEPTIONS, e:
#       error = 'A retriable error occurred: %s' % e

#     if error is not None:
#       print error
#       retry += 1
#       if retry > MAX_RETRIES:
#         exit('No longer attempting to retry.')

#       max_sleep = 2 ** retry
#       sleep_seconds = random.random() * max_sleep
#       print 'Sleeping %f seconds and then retrying...' % sleep_seconds
#       time.sleep(sleep_seconds)

# if __name__ == '__main__':
#   parser = argparse.ArgumentParser()
#   parser.add_argument('--file', required=True, help='Video file to upload')
#   parser.add_argument('--title', help='Video title', default='Test Title')
#   parser.add_argument('--description', help='Video description',
#     default='Test Description')
#   parser.add_argument('--category', default='22',
#     help='Numeric video category. ' +
#       'See https://developers.google.com/youtube/v3/docs/videoCategories/list')
#   parser.add_argument('--keywords', help='Video keywords, comma separated',
#     default='')
#   parser.add_argument('--privacyStatus', choices=VALID_PRIVACY_STATUSES,
#     default='private', help='Video privacy status.')
#   args = parser.parse_args()

#   youtube = get_authenticated_service()

#   try:
#     initialize_upload(youtube, args)
#   except HttpError, e:
#     print 'An HTTP error %d occurred:\n%s' % (e.resp.status, e.content)