import os
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# load the .env file variables
load_dotenv()

CLIENT_ID = 'b389b433000a4c8db1129a3ea1460a50'
CLIENT_SECERT = '9e164c0d888d4d1babe450ff57df7778'

client_id = os.environ.get("CLIENT_ID")
client_secert = os.environ.get("CLIENT_SECERT")
client_credentials_manager = SpotifyClientCredentials(client_id, client_secert)
connection = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

print(connection)

sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
result = sp.artist_top_tracks("")
print(type(result["tracks"]))
tracks - result["track"][0:10]
print(tracks)
sub_tracks = [(d["song"],d["popularity"], d["duration"]) for d in tracks]

df = pd.DataFrame(sub_tracks)
print(df)