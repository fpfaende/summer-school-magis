#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import csv

url = '''https://api.meetup.com/2/cities?&sign=true&photo-host=public&country=fr&page=20'''

result = requests.get(url)
print result.status_code
data = result.json()

rows = []

for city in data['results']:
		row = [city['city'].encode('utf-8'), city['lat'], city['lon'], city['member_count']]
		rows.append(row)

while len(data['meta']['next']) > 0 :
	result = requests.get(data['meta']['next'])
	data = result.json()
	for city in data['results']:
		row = [city['city'].encode('utf-8'), city['lat'], city['lon'], city['member_count']]
		rows.append(row)


with open('some.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(rows)