import requests, json

token_url = "https://accounts.spotify.com/api/token"

credentials_file = 'auth/app_credentials.txt'
with open(credentials_file, 'r') as cred_file:
    creds = cred_file.read()

payload = "grant_type=client_credentials&undefined="
headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'Authorization': "Basic " + creds,
    'cache-control': "no-cache"
    }

response = requests.request("POST", token_url, data=payload, headers=headers)
token = json.loads(response.text)['access_token']
print(token)