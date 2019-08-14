from plexapi.server import PlexServer
from plexapi.playlist import Playlist
import os
import sys

#PLEX INFO
url = "http://192.168.1.#:32400"
token = "##################"

if hasattr(__builtins__, 'raw_input'):
        input=raw_input

plex = PlexServer(url, token)
for i, playlist in enumerate(plex.playlists()):
        print("{position}) {playlist_title}".format(position=i+1, playlist_title=playlist.title))
choice = -1
while choice == -1:
        selection = input("Select playlist: ")
        try:
                selection = int(selection)
                if selection > 0 and selection <= i+1:
                        choice = selection - 1
                else:
                        print("Invalid selection")
        except:
                print("Invalid selection")
new_playlist_name = input("Enter new playlist name: ")
try:
    Playlist.create(plex, new_playlist_name, plex.playlists()[choice].items())
    print("{playlist} created".format(playlist=new_playlist_name))
except:
    print("Error")

