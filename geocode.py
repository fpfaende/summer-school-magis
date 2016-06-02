#!/usr/bin/python
# -*- coding: utf-8 -*-

import geocoder
import csv

data = []

with open('mes-restaurants.csv','r') as csvfile:
	dialect = csv.Sniffer().sniff(csvfile.read(1024))
	csvfile.seek(0)
	reader = csv.reader(csvfile, dialect)
	for row in reader:
		myrow = row
		address = row[1]
		g = geocoder.google(address)
		myrow.append(g.latlng[0])
		myrow.append(g.latlng[1])
		data.append(myrow)
print data
with open('mes-restaurants-geocoded.csv','wb') as csvfile:
	writer = csv.writer(csvfile, delimiter=';')
	writer.writerows(data)