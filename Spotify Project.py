import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
from google.cloud import bigquery

# spotify credentials
spClientId = '61fabd63168841eebb2b778fa46f1761'
spClientSecret = 'b0371d63aa584bc5b16e9292bd2ebdba'
client_credentials_manager = SpotifyClientCredentials(
    client_id=spClientId, client_secret=spClientSecret)

# username and scope
username = 'andreyooow'
scope = 'playlist-read-private user-read-private app-remote-control user-read-currently-playing user-read-playback-state user-modify-playback-state'
sp_c = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
token = util.prompt_for_user_token(username, scope=scope, client_id=spClientId,
                                   client_secret=spClientSecret, redirect_uri='http://localhost:8080/')
sp = spotipy.Spotify(
    auth=token, client_credentials_manager=client_credentials_manager)


results = sp.current_user_recently_played(limit=50)
print(results)
