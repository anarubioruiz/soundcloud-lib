# Soundcloud-lib
This is a Soundcloud API library that doesn't require a client ID to function.  It's basic, it can really only fetch tracks and playlists, but doesn't require the user to go through the soundcloud app approval process.
Forked from: https://github.com/3jackdaws/soundcloud-lib

# Features
* Does not require a client ID
* Fetches and writes mp3 metadata (Album artist, title, artwork)
* Can fetch entire playlists of tracks

# Requeriments
* deb: python3-mutagen
* deb: python3-bs4

# How
This library uses **programming** and **algorithms** to find a client ID that can be used to access the Soundcloud API.

## Saving an mp3 to a file.
This will write the ID3 tags for album artist, track title AND will embed the album artwork into the mp3.
```python
from sclib import SoundcloudAPI, Track, Playlist

api = SoundcloudAPI()  # never pass a Soundcloud client ID that did not come from this library

track = api.resolve('https://soundcloud.com/itsmeneedle/sunday-morning')

assert type(track) is Track

filename = f'./{track.artist} - {track.title}.mp3'

with open(filename, 'wb+') as fp:
    track.write_mp3_to(fp)

```

## Fetch a playlist

```python
from sclib import SoundcloudAPI, Track, Playlist

api = SoundcloudAPI()
playlist = api.resolve('https://soundcloud.com/playlist_url')

assert type(playlist) is Playlist

for track in playlist.tracks:
    filename = f'./{track.artist} - {track.title}.mp3'
    with open(filename, 'wb+') as fp:
        track.write_mp3_to(fp)

```

## Write Album Name or Track Number
```python
from sclib import SoundcloudAPI, Track, Playlist

playlist = SoundcloudAPI().resolve("https://soundcloud.com/user/sets/playlist_name")

for track_number, track in enumerate(playlist):
    track.track_no = track_number
    track.album = playlist.title
    with open(f"{track.artist} - {track.title}.mp3", "wb+") as file:
        track.write_mp3_to(file)
```

# Known Bugs

### This library cannot download tracks that are not marked "Downloadable". 
"Downloadable" tracks have an MP3 representation while non-"Downloadable" ones only have HLS representations.  I would like to add HLS assembly to this library in the future.
