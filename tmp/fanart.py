# -*- coding: utf-8 -*-
import re, os, json, math, io, sys
import requests
from time import time, localtime, strftime, sleep, gmtime, mktime
from datetime import datetime, timedelta, date
import base64
from marshal import loads
from sys import version_info
py3 = version_info[0] == 3
try:
	if py3:
		from _thread import start_new_thread
		from urllib.request import urlopen, quote
	else:
		from thread import start_new_thread
		from urllib2 import urlopen, quote
except:
	pass
try:
	from urllib.request import Request, urlopen  # Python 3
except ImportError:
    from urllib2 import Request, urlopen  # Python 2
header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36", "accept": "application/json"}
# print(dir(os))
print("\U0001F600")
tmdb_api = "3c3efcf47c3577558812bb9d64019d65"
tvdb_api = "a99d487bb3426e5f3a60dea6d3d3c7ef"
fanart_api = "6d231536dea4318a88cb2520ce89473b"
# "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzYzNlZmNmNDdjMzU3NzU1ODgxMmJiOWQ2NDAxOWQ2NSIsInN1YiI6IjVkZGQ3MmM1YTgwNjczMDAxMjEzOGY5NSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.B0QKYo7JzTG4VbOatyHhxDtVqbacUdLMd-Dn-VAWBbE"
########################################################################################################################
title="Navy CIS"
lang="en"
srch="tv"
# url_tmdb = "https://api.themoviedb.org/3/search/{}?api_key={}&language={}&query={}".format(srch, tmdb_api, lang, title)
# data = requests.get(url_tmdb, stream=True, allow_redirects=True, headers=header).json()
# id = data["results"][0]["id"]
# # print(data)
#
# url = 'https://api.themoviedb.org/3/{}/{}?&api_key={}&append_to_response=external_ids'.format(srch, id, tmdb_api)
# data2 = requests.get(url, stream=True, allow_redirects=True, headers=header).json()
# #
# # id = data2["external_ids"]
# # print(id)
# id = data2["external_ids"]['tvdb_id']
#
# url = "https://webservice.fanart.tv/v3/{}/{}?api_key={}".format(srch, id, fanart_api)
# data = requests.get(url, stream=True, allow_redirects=True, headers=header).json()
#
# # print(data)
# dwnldFile="./tmp/{}.jpg".format(title)
# url = data['tvposter'][0]['url']
# print(url)




# open(dwnldFile, 'wb').write(requests.get(url, stream=True, allow_redirects=True, verify=False).content)


# with open(dwnldFile, 'wb') as f:
#     f.write(requests.get(url, stream=True, allow_redirects=True, headers=header).content)


try:
	url_tmdb = "https://api.themoviedb.org/3/search/{}?api_key={}&language={}&query={}".format(srch, tmdb_api, lang,
																							   title)
	data = requests.get(url_tmdb, stream=True, allow_redirects=True, headers=header).json()
	tmdb_id = data["results"][0]["id"]
	url = 'https://api.themoviedb.org/3/{}/{}?&api_key={}&append_to_response=external_ids'.format(srch, tmdb_id,
																								  tmdb_api)
	data2 = requests.get(url, stream=True, allow_redirects=True, headers=header).json()
	if srch == "movie":
		try:
			id = data2["external_ids"]['imdb_id']
		except:
			id = tmdb_id
		srch = "movies"
	else:
		id = data2["external_ids"]['tvdb_id']
except:
	id = None


if srch == "movie":
	srch = "movies"
url = "https://webservice.fanart.tv/v3/{}/{}?api_key={}".format(srch, id, fanart_api)
data = requests.get(url, stream=True, allow_redirects=True, headers=header).json()
print(data)
url = data['tvposter'][0]['url']
print(url)








