import os
import sys
import numpy as np
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials



load_dotenv()

CLIENT_ID='b389b433000a4c8db1129a3ea1460a50'
CLIENT_SECRET='9e164c0d888d4d1babe450ff57df7778'


CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

if not CLIENT_ID or not CLIENT_SECRET:
    raise ValueError("CLIENT_ID and CLIENT_SECRET must be set in the .env file")

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

print(sp)


artist_id = "4tZwfgrHOc3mvqYlEYSvVi" 
result = sp.artist_top_tracks(artist_id)

print(type(result["tracks"]))
tracks = result["tracks"][0:10]
print(tracks)

sub_tracks = [(d["name"], d["popularity"], d["duration_ms"]) for d in tracks]

df = pd.DataFrame(sub_tracks, columns=["Song", "Popularity", "Duration"])
print(df)
