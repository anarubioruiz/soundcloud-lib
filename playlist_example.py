#!/usr/bin/python3
# -*- coding:utf-8; mode:python -*-

import os
import errno
from sclib import SoundcloudAPI, Track, Playlist

api = SoundcloudAPI()
playlist = api.resolve('https://soundcloud.com/laruedas/sets/top')
downloads_dir = 'downloads/'

assert type(playlist) is Playlist

if not os.path.exists(os.path.dirname(downloads_dir)):
        try:
            os.makedirs(os.path.dirname(downloads_dir))
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise

for track in playlist.tracks:
    filename = f'{track.artist} - {track.title}.mp3'
    print(filename)
    with open(f'{downloads_dir}{filename}', 'wb+') as fp:
        track.write_mp3_to(fp)