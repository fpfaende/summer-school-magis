#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import random
import time
import csv

data = []

headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.36 Safari/537.36'}
cookies = {'CC':'15101-cfd', 'expires':'Sat, 04-Jun-2016 10:19:05 GMT', 'Max-Age':'172799', 'path':'/'}

for page in range(1,28):

	url = 'http://www.lafourchette.com/restaurant+lyon'
	payload = {'page':page}
	print 'getting',url
	r = requests.get(url,headers=headers, cookies = cookies, params=payload)

	soup = BeautifulSoup(r.text, 'html5lib')

	itemCount = len(soup.find_all('h3','resultItem-name'))
	restaurantsName = soup.find_all('h3','resultItem-name')
	restaurantsAddress = soup.find_all('div','resultItem-address')
	restaurantsRating = soup.find_all('span','rating-ratingValue')
	for i in range(0,itemCount):
		name = restaurantsName[i].get_text().encode('utf-8')
		address = restaurantsAddress[i].contents[0].encode('utf-8').strip()
		try:
			rating = restaurantsRating[i].contents[0].encode('utf-8').strip()
		except Exception, e:
			rating = None
			
		data.append({'name':name, 'address':address, 'rating':rating})

	sleeptime = random.uniform(0.5,1.0)
	time.sleep(sleeptime)

with open('mes-restaurants.csv','w') as csvfile:
	fieldnames = ['name', 'address', 'rating']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	for restaurant in data:
		writer.writerow(restaurant)
	