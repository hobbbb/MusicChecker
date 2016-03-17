# -*- coding: utf-8 -*-
import urllib
import xmltodict
import json

api_url = 'https://musicbrainz.org/ws/2/'

def _request(method, params):
    if not method or type(params) != dict:
        print 'Error'
        return

    enc_params = []
    for k in params:
        if type(params[k]) == str:
            enc_params.append(urllib.urlencode({ k: params[k].encode('utf-8') }))
        else:
            enc_params.append("{0}={1}".format(k, params[k]))

    url = api_url + "{0}?{1}".format(method, "&".join(enc_params))
    resp = urllib.urlopen(url)

    xml_string = resp.read()
    data = xmltodict.parse(xml_string)
    print json.dumps(data, indent=4)

    return data

def get_albums_by_artist(mbid):
    return _request(method='release-group', params={ 'type': 'album', 'artist': mbid })

