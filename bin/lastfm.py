#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import django
import time
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

os.environ['DJANGO_SETTINGS_MODULE'] = 'music.settings'
django.setup()

import music.API.LastFm
import musicbrainzngs
# import music.API.Musicbrainz
from music.collection.models import Artist, Album

musicbrainzngs.set_useragent(
    "my_music_collection",
    "0.1",
)

def ImportLibrary():
    res = music.API.LastFm.library_get_artists(user='Holbutla', page=1000)
    pages_cnt = res['lfm']['artists']['@totalPages']
    for p in range(1, int(pages_cnt) + 1):
        res = music.API.LastFm.library_get_artists(user='Holbutla', page=p)

        lf_artists = res['lfm']['artists']['artist']
        for lfa in lf_artists:
            name = lfa.get('name', '')
            mbid = lfa.get('mbid', '')

            artist = Artist.objects.filter(name=name)
            if len(artist) == 1:
                print 'Update: ' + name
                artist[0].mbid = mbid
                artist[0].save()
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

def GetAlbumsOfArtist(artist_mbid):
    artist = Artist.objects.filter(mbid=artist_mbid)
    if len(artist) != 1:
        return

    # musicbrainzngs.get_release_group_by_id(id, includes=[], release_status=[], release_type=[])
    res = musicbrainzngs.get_artist_by_id(artist_mbid, includes=['releases'])
    print res

    """
    res = music.API.Musicbrainz.get_albums_by_artist(artist_mbid)
    data = res.get('metadata', '')
    if not data:
        return

    mb_albums = data['release-group-list']['release-group']
    for mba in mb_albums:
        name = mba.get('title', '')
        date = mba.get('first-release-date', '')
        album_mbid = mba.get('@id', '')

        album = Album.objects.filter(artist=artist, mbid=album_mbid)
        if len(album) == 1:
            print 'Update: ' + name
            album[0].mbid = album_mbid
            album[0].year = ''
            album[0].save()
        elif len(album) == 0:
            print 'Add: ' + name
            album = Album(
                artist=artist,
                name=name,
                year='',
                mbid=album_mbid,
                lastfm_check=1,
            )
            album.save()
        else:
            print 'Error: ' + name
    """


# ImportLibrary()
GetAlbumsOfArtist('ef58d4c9-0d40-42ba-bfab-9186c1483edd')




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

