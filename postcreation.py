from sm_authentication import get_MetaCreds


def postcreation():

    creds = get_MetaCreds()
    #print(creds['access_token'])
    

postcreation()
