import requests
import json
from authenticate import get_token
import time, datetime
import os

url = 'https://api.spotify.com/v1/me/player'

#get a token
token = get_token()
print("getting token...")

def main():
    header = {'Authorization': 'Bearer ' + token}
    resp = requests.get(url=url, headers=header)
    data = json.loads(resp.text)

    device_name = (data['device'])['name']

    song_length = int((data['item'])['duration_ms']/1000)
    song_progress = int(data['progress_ms']/1000)
    song_percentage = int((song_progress / song_length) * 100)

    song_artist = data['item']['artists'][0]['name']
    song_name = (data['item'])['name']

    progress_24 = '#'*song_percentage + ('-'*(24-song_percentage))
    
    print('Playing on: ' + device_name)
    print(song_artist)
    print(song_name)
    print(str(datetime.timedelta(seconds=song_progress)) + '/' + str(datetime.timedelta(seconds=song_length)))
    print()
    time.sleep(1)


while True:
    try:
        main()
        time.sleep(0.1)
    except KeyboardInterrupt:
        print("bye")
        raise SystemExit