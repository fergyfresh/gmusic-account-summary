import json
import heapq
from datetime import datetime


def import_my_activity(path):
    return json.load(open(path))


def clean_activities(activity):
    songs = []
    searches = []
    for i in activity:
        if 'description' in i and 'title' in i and 'Searched' not in i:
            songs.append({'artist': i['description'], 'title': i['title'].replace('Listened to ', ''), 'time':i['time']})
        else:
            searches.append(i)
    return songs, searches


def top_n_songs(songs, n, start=None, end=None):
    song_map = {}
    for song in songs:
        timestamp = datetime.fromisoformat(song['time'].replace('Z', ''))
        if is_valid_date(timestamp, start, end):
            title = song['title']
            if title not in song_map:
                song_map[title] = 1
            else:
                song_map[title] += 1
    top_n_keys = heapq.nlargest(n, song_map, key=song_map.get)
    output = {}
    for i in top_n_keys:
        output[i] = song_map[i]
    return output


def get_artist(activity):
    artist = None
    if 'artist' in activity:
        artist = activity['artist']
    elif 'description' in activity:
        artist = activity['description']
    else:
        print(activity)
    return artist


def top_n_artists(songs, n, start=None, end=None):
    song_map = {}
    for song in songs:
        timestamp = datetime.fromisoformat(song['time'].replace('Z', ''))
        if is_valid_date(timestamp, start, end):
            artist = get_artist(song)
            if artist not in song_map:
                song_map[artist] = 1
            else:
                song_map[artist] += 1
    return heapq.nlargest(n, song_map, key=song_map.get)


def is_valid_date(timestamp, start: datetime=None, end: datetime=None):
    if start and timestamp < start or end and timestamp > end:
        return False
    return True


def sweep_the_years(songs, top_n= 5, x_years_to_sweep=10):
    ds = datetime(2019, 1, 1)
    de = datetime(2020, 1, 1)
    sweep = {}
    for i in range(x_years_to_sweep):
        top_artists = top_n_artists(songs, top_n, ds, de)
        if top_artists:
            sweep[ds] = top_artists
        ds = ds.replace(year=ds.year - 1)
        de = de.replace(year=de.year - 1)
    return sweep