#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import csv

r = requests.get('http://www.lafourchette.com/restaurant+lyon')

soup = BeautifulSoup(r.text.encode('utf-8'), 'html.parser')

restaurantsName = soup.find_all('h3','resultItem-name')
restaurantsAddress = soup.find_all('div','resultItem-address')
restaurantsRating = soup.find_all('span','rating-ratingValue')
count = len(restaurantsName)
data = []

for i in range(0,count):
	name = restaurantsName[i].get_text().encode('utf-8')
	address = restaurantsAddress[i].get_text().encode('utf-8').strip()
	rating = restaurantsRating[i].get_text().encode('utf-8')
	row = [name, address, rating]
	data.append(row)

with open('restaurant-in-lyon.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(data)


