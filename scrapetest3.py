from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html.read())

for child in bsObj.find("table",{"id":"giftList"}).children:
	print(child)

with open("relativi","xt") as fout:
	fout.write(child)
