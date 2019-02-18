import requests

url = "https://api.spotify.com/v1/me/player/next"
TOKEN_FILE = 'auth/token'

#read token from file
with open(TOKEN_FILE, 'r') as file:
    TOKEN = file.read()

headers = {
    'Accept': "application/json",
    'Content-Type': "application/json",
    'Authorization': "Bearer " + TOKEN
    }

response = requests.request("POST", url, headers=headers)

print(response.text)