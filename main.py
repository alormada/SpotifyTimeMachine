import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

load_dotenv()
SPOTIFY_CLIENT_ID=os.environ["SPOTIFY_CLIENT_ID"]
SPOTIFY_CLIENT_SECRET=os.environ["SPOTIFY_CLIENT_SECRET"]
SPOTIFY_USERNAME=os.environ["SPOTIFY_USERNAME"]


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username=SPOTIFY_USERNAME,
    )
)
user_id = sp.current_user()["id"]

DATE = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# DATE = "2025-03-27"
URL = f"https://www.billboard.com/charts/hot-100/{DATE}"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

webpage = requests.get(URL, headers=header)
soup = BeautifulSoup(webpage.text, "html.parser")

excluded_words = ['Songwriter(s):', 'Producer(s):', 'Imprint/Promotion Label:', 'Gains in Weekly Performance', 'Additional Awards']

titles = []
for title in soup.find_all(name="h3", id="title-of-a-story"):
    try:
        if title.string.replace("\n", "").replace("\t", "") not in excluded_words:
            titles.append(title.string.replace("\n", "").replace("\t", ""))
    except:
        pass
# artists = [title.next_sibling for title in soup.find_all(name="h3", id="title-of-a-story") if title.string.replace("\n", "").replace("\t", "") not in excluded_words]

titles = titles[0:20]

print(titles)
# print(artists)

# query = {"track": titles[0]}
# print(query)
# track = sp.search(q=titles[0], limit=1, type="track")["tracks"]["items"][0]["uri"]
# pprint.pp(track)

tracks = [sp.search(q=track, limit=1, type="track")["tracks"]["items"][0]["uri"] for track in titles]
print(tracks)

playlist_name = f"{DATE} Billboard 100"

playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)

playlist_id = playlist["id"]

sp.playlist_add_items(playlist_id=playlist_id, items=tracks)