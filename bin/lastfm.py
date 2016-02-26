#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import django
import time
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

os.environ['DJANGO_SETTINGS_MODULE'] = 'music.settings'
django.setup()

import music.collection.LastFmApi
from music.collection.models import Artist, Album

def ImportLibrary():
    res = music.collection.LastFmApi.library_get_artists(user='Holbutla', page=1000)
    pages_cnt = res['lfm']['artists']['@totalPages']
    for p in range(1, int(pages_cnt) + 1):
        res = music.collection.LastFmApi.library_get_artists(user='Holbutla', page=p)

        lf_artists = res['lfm']['artists']['artist']
        for lfa in lf_artists:
            name = lfa['name']
            mbid = lfa['mbid'] or ''

            artist = Artist.objects.filter(name=name)
            if len(artist) == 1:
                print 'Update: ' + name
                # artist.mbid = lfa['mbid']
                # artist.save()
            elif len(artist) == 0:
                print 'Add: ' + name
                artist = Artist(
                    name=name,
                    mbid=mbid,
                    lastfm_check=1,
                )
                artist.save()
            else:
                print 'Error: ' + name

ImportLibrary()

"""
def CheckArtists():
    artists = Artist.objects.filter(lastfm_check=0)
    for art in artists:
        resp = urllib.urlopen(api_url + "autocorrect=0&method=artist.getInfo&%s" % urllib.urlencode({'artist': art.name.encode('utf-8')}))
        xml_string = resp.read()

        try:
            root = xml.etree.ElementTree.fromstring(xml_string)
        except xml.etree.ElementTree.ParseError:
            print 'ERROR: ' + art.name
            continue

        lastfm_name = root.find('artist').find('name').text
        print lastfm_name + ' --- ' + art.name

        if lastfm_name:
            art.lastfm_check = 1
            art.save()

        time.sleep(2)

def CheckAlbums():
    albums = Album.objects.filter(lastfm_check=0)
    for alb in albums:
        resp = urllib.urlopen(api_url + "autocorrect=0&method=album.getInfo&%s&%s" % (urllib.urlencode({'artist': alb.artist.name.encode('utf-8')}), urllib.urlencode({'album': alb.name.encode('utf-8')})))
        xml_string = resp.read()

        try:
            root = xml.etree.ElementTree.fromstring(xml_string)
        except xml.etree.ElementTree.ParseError:
            print "ERROR: %s %s" % (alb.name, alb.artist.name)
            continue

        lastfm_name = root.find('album').find('name').text
        print lastfm_name + ' --- ' + alb.name

        if lastfm_name:
            alb.lastfm_check = 1
            alb.save()

        time.sleep(2)

# CheckArtists()
# CheckAlbums()
"""

