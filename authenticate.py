import requests, json, os

#token_url = "https://accounts.spotify.com/api/token"

#credentials_file = 'auth/app_credentials.txt'
token_file = 'auth/token'

def get_token():
    with open(token_file, 'r') as tf:
        token = tf.read()
    '''
    payload = "grant_type=client_credentials&undefined="
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'Authorization': "Basic " + creds,
        'cache-control': "no-cache"
        }

    response = requests.request("POST", token_url, data=payload, headers=headers)
    token = json.loads(response.text)['access_token']
    '''
    return token