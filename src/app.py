import os
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import spotify
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")



client_credential_manager = SpotifyClientCredentials(client_id=os.getenv("CLIENT_ID"), client_secret=os.getenv("CLIENT_SECRET")) 

sp = spotipy.Spotify(client_credentials_manager=client_credential_manager)

Kendrick_uri = '2YZyLoL8N0Wb9xBt1NhZWg'
spotipy.Spotify(client_credentials_manager = client_id)