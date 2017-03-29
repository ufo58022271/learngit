from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

def getTitle(url):
	try:
		html = urlopen(url)
	except (HTTPError,URLError) as e:
		return none
	try:
		bsObj = BeautifulSoup(html.read())
		title = bsObj.h1
	except AttributeError as e:
		return none
	return title
title = getTitle("http://pythonscraping.com/pages/page1.html")
if title == none:
	print("Title could not be found")
else:
	print(title)