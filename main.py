import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth


def get_top_100(date):
    url = f"https://www.billboard.com/charts/hot-100/{date}/"

    response = requests.get(url=url)
    contents = response.text

    soup = BeautifulSoup(contents, "html.parser")

    song_titles = soup.select(selector="ul li #title-of-a-story")

    #print(song_titles)
    top_100 = []

    for song in song_titles:
        # print(song.getText())
        top_100.append(song.getText().strip())

    return top_100

def create_playlist(date):
    scope = "playlist-modify-private"
    name = f"Api top 100 {date}"
    new_playlist = {
        "name": name,
        "description": "Api playlist",
        "public": False
    }

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    print(sp.current_user())

    user_id = sp.current_user()['id']
    playlist = sp.user_playlist_create(user=user_id, name=new_playlist["name"], public=new_playlist["public"], collaborative=False, description=new_playlist["description"])

    return playlist

def add_songs_to_playlist(playlist, songs):
    scope = "playlist-modify-private"

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    top_100_songs_id = []
    for song in songs:
        track_id = sp.search(q=' track:' + song, type='track')
        if len(track_id['tracks']['items']) != 0:
            top_100_songs_id.append(track_id['tracks']['items'][0]['id'])
            print(f"{len(track_id)} : {track_id['tracks']['items'][0]['id']} : {song}")

    sp.playlist_add_items(playlist['id'], top_100_songs_id)


year = input("From which year would u like to create the playlist. Type the data in the YYYY-MM-DD: ")

top_100_songs = get_top_100(year)

print(top_100_songs)

playlist = create_playlist(year)
add_songs_to_playlist(playlist, top_100_songs)
