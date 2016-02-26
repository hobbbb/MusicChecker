#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import django
import urllib
import time
import xml.etree.ElementTree
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

os.environ['DJANGO_SETTINGS_MODULE'] = 'music.settings'
django.setup()

from music.collection.models import Artist, Album

"""
Application name    hobbbb app
API key 5c6346142584adb62a03f005a8fab87a
Shared secret   19677377de7cf8f9cec47f884925d18d
Registered to   Holbutla
"""

api_url = 'http://ws.audioscrobbler.com/2.0/?user=Holbutla&api_key=5c6346142584adb62a03f005a8fab87a&'

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

CheckArtists()
CheckAlbums()
