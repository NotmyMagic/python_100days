from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

time_travel = input("Which year do you want to travel to? Use this YYY-MM-DD format: ")

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
url = f"https://www.billboard.com/charts/hot-100/{time_travel}"


# use with open instead to access an html thats not live
response = requests.get(url=url, headers=headers)
BB_hot_100 = response.text

soup = BeautifulSoup(BB_hot_100, "html.parser")
song_names_raw = soup.select("li ul li h3")
song_names = [song.get_text().strip() for song in song_names_raw]



sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com",
        client_id="81e87c02e82146049db858795845410b",
        client_secret="f941c992810845f2bafc50b114eb64d6",
        show_dialog=True,
        cache_path="./part5/spotify_timetravel/token.txt",
        username="NotmyMagic"
        ))

user_id = sp.current_user()["id"]
print(user_id)

song_uris = []
year = time_travel.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

sp.playlist_add_items(playlist_id="27z4L6xje9rR4JStVAmzG8", items=song_uris)