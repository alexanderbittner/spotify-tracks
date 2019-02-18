import requests
import json

url = 'https://api.spotify.com/v1/me/player'

#get a token
token_url = 'https://accounts.spotify.com/api/token' #expires after an hour!
token = requests.post(token_url, )


header = {'Authorization': 'Bearer ' + token}

resp = requests.get(url=url, headers=header)
data = json.loads(resp.text)

device_name = (data['device'])['name']

song_length = (data['item'])['duration_ms']
song_progress = data['progress_ms']
song_percentage = int((song_progress / song_length) * 24)

song_artist = data['item']['artists'][0]['name']
song_name = (data['item'])['name']

progress_24 = '#'*song_percentage + ('-'*(24-song_percentage))

first_row = (device_name[:24] + '\\') if len(device_name) > 24 else device_name
second_row = (song_artist[:24] + '..') if len(song_artist) > 24 else song_artist
third_row = (song_name[:24] + '\\') if len(song_name) > 24 else song_name
fourth_row = (progress_24[:24] + '\\') if len(progress_24) > 24 else progress_24

print(first_row)
print(second_row)
print(third_row)
print(fourth_row)