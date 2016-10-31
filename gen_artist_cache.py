#!/usr/bin/python
import json
import requests
import os.path

# my entire playlist archive, exported from
# http://www.spotmybackup.com/
ARTIST_CACHE="artist_cache.txt"

def make_artist_cache(): 
    spotify_f = open("spotify_2016_10_31.json");
    
    # open the playlist as json
    playlists = json.load(spotify_f)
    
    artist_f = open("artists_cache.txt", "w")
    
    # Now, these playlists only have track IDs in them 
    # then list the bands in the playlist
    for song in playlists['playlists']['IA 2016 Favorites']['tracks']:
        r = requests.get('https://api.spotify.com/v1/tracks/' + song["id"])
        artist_f.write(r.json()["artists"][0]["name"].encode("utf8"))
        artist_f.write("\n")

if not os.path.isfile(ARTIST_CACHE):
    make_artist_cache()

        # and then find those bands in the schedule

# and export them

