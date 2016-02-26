# -*- coding: utf-8 -*-
import urllib
import xmltodict
import json

"""
Application name    hobbbb app
API key 5c6346142584adb62a03f005a8fab87a
Shared secret   19677377de7cf8f9cec47f884925d18d
Registered to   Holbutla
"""

api_url = 'http://ws.audioscrobbler.com/2.0/?api_key=5c6346142584adb62a03f005a8fab87a&'

def _request(method, params):
    if not method or type(params) != dict:
        print 'Error'
        return

    enc_params = []
    for k in params:
        if type(params[k]) == str:
            enc_params.append(urllib.urlencode({ k: params[k].encode('utf-8') }))
        else:
            enc_params.append("%s=%s" %(k, params[k]))

    url = api_url + "method=%s&%s" % (method, "&".join(enc_params))
    resp = urllib.urlopen(url)

    xml_string = resp.read()
    data = xmltodict.parse(xml_string)
    # print json.dumps(data, indent=4)

    return data

def library_get_artists(user, page=1, limit=50):
    return _request(method='library.getArtists', params={ 'user': user, 'page': page, 'limit': limit })

def artist_get_info(user):
    return _request(method='artist.getInfo', params={ 'user': user })

def album_get_info(user):
    return _request(method='lbum.getInfo', params={ 'user': user })
