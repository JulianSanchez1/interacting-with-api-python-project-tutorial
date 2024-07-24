import os
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

if not CLIENT_ID or not CLIENT_SECRET:
    raise ValueError("CLIENT_ID and CLIENT_SECRET must be set in the .env file")

# Set up Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def fetch_top_tracks(artist_id):
    try:
        result = sp.artist_top_tracks(artist_id)
        tracks = result['tracks']
        sub_tracks = [
            {
                "Song": track["name"],
                "Popularity": track["popularity"],
                "Duration": track["duration_ms"]
            }
            for track in tracks
        ]
        df = pd.DataFrame(sub_tracks)
        return df
    except spotipy.SpotifyException as e:
        print(f"Spotify API error: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error

# Example artist ID
artist_id = "7dGJo4pcD2V6oG8kP0tJRR"  # Replace with a valid artist ID
df = fetch_top_tracks(artist_id)

# Sort by popularity and display top 3
df_sorted = df.sort_values(by="Popularity", ascending=False)
top_3_songs = df_sorted.head(3)
print("Top 3 Songs by Popularity:")
print(top_3_songs)



