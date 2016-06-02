#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json
import csv

url = 'https://api.flickr.com/services/rest/'
payload = {
	'method':'flickr.photos.search',
	'api_key':'2d5481f4b9e0d48f5f3ec89c76ad3dae',
	'has_geo':'true',
	'extras':'geo,tags',
	'format':'json',
	'woe_id':'12597165'
}

r = requests.get(url, params=payload)
print r.status_code
print r.text[14:][:-1]
results = json.loads(r.text[14:][:-1])

with open('geomatic.csv', 'wb') as csvfile:
	geomaticWriter = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	for photo in results['photos']['photo']:
		geomaticWriter.writerow([photo['longitude'], photo['latitude'], photo['title'].encode('utf-8'), photo['tags'].encode('utf-8')])
print 'done' 
