#!/usr/bin/env python
import os
import sys
import django
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

os.environ['DJANGO_SETTINGS_MODULE'] = 'music.settings'
django.setup()

from music.collection.models import Artist, Album

f = open('/Users/hob/Downloads/music.txt')

rows = []
for line in f:
    rows = line.split("\r");

music = {}
for r in rows[1:]:
    cols = r.split("\t");
    if not cols[0]:
        break

    artist = cols[1]
    album  = cols[3]
    year   = cols[12]

    if artist not in music:
        music[artist] = {}

    music[artist][year] = album

for art in sorted(music):
    artist = Artist.objects.filter(name=art)

    """
    try:
        artist = Artist.objects.get(name=art)
    except Artist.DoesNotExist:
        artist = Artist(name=art)
        artist.save()
    """

    for y in sorted(music[art]):
        list = Album.objects.filter(name=music[art][y], artist=artist)
        print list[1]
        """
        album = list[0]
        if year not in album:
            album.year = y
            album.save()
        """

        """
        try:
            album = Album.objects.get(name=alb, artist=artist)
        except Album.DoesNotExist:
            album = Album(name=alb, artist=artist)
            album.save()
        """

f.close()
