import requests
import json

url = 'https://api.spotify.com/v1/me/player'
token = 'BQCrH0OsHSWuNB0MOe0nPmTZ9d42uRQFpmbtG0ajIbRVatiNjujzdv1mxvhHkaMRi5k_YKUuGyX1nw6ry_hyqlbRMCBqTbqdjq-DbJQd3EAU9LD9ZzhfAdEqzYuJWrOK1TrroBKYn2W9gSC05aTaxHAqU87m6f-Gxw'
header = {'Authorization': 'Bearer ' + token}


#resp = requests.get(url=url, params=params)
resp = requests.get(url=url, headers=header)
data = json.loads(resp.text)

#print(type(data))
# data is a dict

#for key, value in data.items():
#    print("    " + str(type(key)) + ", " + key)
#    print("        " + str(type(value)) + ", " + str(value))

#device = data['device']
#print(device)
device_name = (data['device'])['name']

song_length = (data['item'])['duration_ms']
song_progress = data['progress_ms']
song_percentage = int((song_progress / song_length) * 24)

song_artist = data['item']['artists'][0]['name']
song_name = (data['item'])['name']


item = data['item']






progress_24 = '#'*song_percentage + '-'*(24-song_percentage)

first_row = (device_name[:24] + '\\') if len(device_name) > 24 else device_name
second_row = (song_artist[:24] + '..') if len(song_artist) > 24 else song_artist
third_row = (song_name[:24] + '\\') if len(song_name) > 24 else song_name
fourth_row = (progress_24[:24] + '\\') if len(progress_24) > 24 else progress_24



print(first_row)
print(second_row)
print(third_row)
print(fourth_row)



#structure:
#data:dict
#    device:dict
#        name:str
#    progress_ms:int
#    item:dict
#        artists:list
#            artist:dict
#                name:str
#        duration_ms:int
#        name:str
#