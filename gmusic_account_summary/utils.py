#!/usr/bin/env python
# -*- coding: utf-8 -*-
import heapq
from gmusicapi import Mobileclient

def login(device_id):
    api = Mobileclient()
    api.oauth_login(device_id)
    return api

def top10_songs(api):
    songs = api.get_all_songs()
    sorted_songs = sorted(songs, key = lambda i: i.get('playCount', 0))
    top10 = []
    for song in sorted_songs[-10:][::-1]:
        if 'playCount' in song:
            top10.append(
                {'title': song['title'],
                 'artist': song['artist'],
                 'play_count': song['playCount']})
    return top10

def top_n_things(api, thing_name, n_top):
    songs = api.get_all_songs()
    things = {}
    for song in songs:
        if thing_name in song:
            thing = song[thing_name]
            if thing in things and 'playCount' in song:
                things[thing] += song['playCount']
            elif 'playCount' in song:
                things[thing] = song['playCount']
    return heapq.nlargest(n_top, things, key=things.get)
