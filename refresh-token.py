import json
import requests
from urllib.parse import quote
import time

#  Client ID and Secret files
client_id_file = 'auth/client-id'
client_secret_file = 'auth/client-secret'
TOKEN_FILE = 'auth/token'
REFRESH_FILE = 'auth/refresh-token'
#  Client Keys
with open(client_id_file, 'r') as id:
    CLIENT_ID = id.read()

with open(client_secret_file, 'r') as secret:
    CLIENT_SECRET = secret.read()

# Spotify URLS
SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_API_BASE_URL = "https://api.spotify.com"
API_VERSION = "v1"
SPOTIFY_API_URL = "{}/{}".format(SPOTIFY_API_BASE_URL, API_VERSION)

# Server-side Parameters
CLIENT_SIDE_URL = "http://127.0.0.1"
PORT = 876
REDIRECT_URI = "{}:{}/callback/q".format(CLIENT_SIDE_URL, PORT)
SCOPE = "user-read-playback-state"
STATE = ""
SHOW_DIALOG_bool = True
SHOW_DIALOG_str = str(SHOW_DIALOG_bool).lower()

auth_query_parameters = {
    "response_type": "code",
    "redirect_uri": REDIRECT_URI,
    "scope": SCOPE,
    "client_id": CLIENT_ID
}



with open(REFRESH_FILE, 'r') as f:
    refresh_token = f.read()

# Auth Step R: Requests refreshed access token
code_payload = {
    "grant_type": "refresh_token",
    "refresh_token": refresh_token,
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
}
post_request = requests.post(SPOTIFY_TOKEN_URL, data=code_payload)

# Auth Step R1: Tokens are Returned to Application
response_data = json.loads(post_request.text)
access_token = response_data["access_token"]

print('#########################################################################################')
print(' NEW TOKEN ')
print(access_token)

with open(TOKEN_FILE, 'w') as file:
    file.write(access_token)

print('done.')