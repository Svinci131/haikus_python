import random
import string
from bs4 import BeautifulSoup
from urllib2 import urlopen

# def getTextByAuthor(): 
# 	letter = random.choice(string.ascii_letters)
# 	menuUrl = 'http://www.gutenberg.org/browse/authors/'+letter
# 	html = urlopen(menuUrl).read()
# 	soup = BeautifulSoup(html, "lxml")
# 	body = soup.find('div', {'class':'pgdbbyauthor'})
BASE_URL = 'https://www.gutenberg.org'

def randomlyGetAuthor(): 
	letter = random.choice(string.ascii_letters)
	menuUrl = 'http://www.gutenberg.org/browse/authors/'+letter
	html = urlopen(menuUrl).read()
	soup = BeautifulSoup(html, "lxml")
	body = soup.find('div', {'class':'pgdbbyauthor'})
	authors = body.findAll('h2')
	# books = [body.findAll('li', {"class": 'pgdbetext'})
	names = [BASE_URL + li.a["href"] for li in body.findAll('li', {"class": 'pgdbetext'})]
	book = random.choice(names)
	# pgdbbyauthor random h2
	print book

randomlyGetAuthor()
# https://automatetheboringstuff.com/chapter11/