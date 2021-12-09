#!/usr/bin/python3
# -*- coding:utf-8; mode:python -*-

import os
import errno
from sclib import SoundcloudAPI, Track

api = SoundcloudAPI()
downloads_dir = 'downloads/'


def create_downloads_dir():
    try:
        os.makedirs(os.path.dirname(downloads_dir))
    except OSError as exception:
        if exception.errno == errno.EEXIST:
            print(f'"{downloads_dir}" directory already exists.')
            return

        raise exception


def download_mp3(url):
    track = api.resolve(url)
    assert type(track) is Track

    create_downloads_dir()
    filename = f'{track.artist} - {track.title}.mp3'
    filepath = f'{downloads_dir}{filename}'

    print(f'Downloading {filename}...')
    with open(filepath, 'wb+') as fp:
        track.write_mp3_to(fp)
    print(f'DONE!')


download_mp3('https://soundcloud.com/hexagon/alex-adair-make-me-feel-better')