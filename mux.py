#mux.py
import os
from os.path import dirname, join
import app
import json
import requests
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), 'mux.env')
load_dotenv(dotenv_path)
mux_id = os.environ['MUX_TOKEN_ID']
mux_secret = os.environ['MUX_TOKEN_SECRET']

response = None
  
class mux:
    def __init__(self):
        headers = {
            'Content-Type': 'application/json',
        }
        data = '{ "playback_policy": ["public"], "new_asset_settings": { "playback_policy": ["public"] } }'
        response = requests.post('https://api.mux.com/video/v1/live-streams', headers=headers, data=data, auth=(mux_id, mux_secret))
        self.stream_key = (json.loads(response.text))["data"]["stream_key"]
        self.playback_id = (json.loads(response.text))["data"]["playback_ids"][0]["id"]
        self.link = "https://stream.mux.com/" + str(self.playback_id) +".m3u8"
    
  