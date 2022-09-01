import xspf_lib as xspf
import sys
import os

from pathfile import path
if len(sys.argv) > 1:
    playlist_name = sys.argv[1]
    if len(sys.argv) > 2:
        path = sys.argv[2]


search_mode = "DFS"  # DFS (depth first search) / BFS (breadth first search)
playlist_name = os.path.basename(path)


def prototype():

    current_ls = os.listdir(path)
    current_ls.sort()
    tracklist = []
    for d in current_ls:
        current_path = os.path.join(path, d)
        if os.path.isdir(current_path):
            tracks = os.listdir(current_path)
            tracks.sort()
            tracks = [os.path.join(current_path, i) for i in tracks if i.endswith(".mp3")]
            tracklist.extend(tracks)
    print(tracklist)
    return tracklist


tracklist = prototype()
track_instances = []
for track in tracklist:
    print(track)
    title_str = os.path.basename(track)
    track_instances.append(xspf.Track(location=f"file://{track}",
                                      title=title_str))


playlist = xspf.Playlist(title=playlist_name,
                         creator="myself",
                         annotation="",
                         trackList=track_instances)


# def dfs(cp):
#     global tracklist
#     dirs = []
#     files = []
#     for f in os.listdir(cp):
#         if os.path.isdir(f):
#             dirs.append(f)
#         else:
#             files.append(f)
#
#     for f in dirs:
#         dfs(os.path.join(cp, f))
#     tracklist.extend(files)


# run = True
# while run:
#     # open all subdirectories
#     current_ls = os.listdir(current_path)

# print(playlist.xml_string())
# <playlist version="1" xmlns="http://xspf.org/ns/0/"><title>Some Tracks</title><creator>myself</creator><annotation>I did this only for examples!.</annotation><date>2020-02-03T14:29:59.199202+03:00</date><trackList><track><location>file:///home/music/killer_queen.mp3</location><title>Killer Queen</title><creator>Queen</creator><annotation>#2 in GB 1975</annotation><info>https://ru.wikipedia.org/wiki/Killer_Queen</info><image>file:///home/images/killer_queen_cover.png</image><album>Sheer Heart Attack</album><trackNum>2</trackNum><duration>177000</duration></track><track><location>https://freemusic.example.com/loc.ogg</location><location>file:///home/music/anbtd.mp3</location><identifier>id1.group</identifier><title>Another One Bites the Dust</title><creator>Queen</creator><link rel="link.namespace">link.uri.info</link><meta rel="meta.namespace">METADATA_INFO</meta></track></trackList></playlist>
playlist.write(f"{playlist_name}.xspf")
