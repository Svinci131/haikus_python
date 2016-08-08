import random
import string
from bs4 import BeautifulSoup
import urllib2
import sys
basePath = '/Users/samanthavinci/Desktop/literaryHaiku/scripts/'
sys.path.append(basePath+'readFile')
from readFile import readFile 


def getTextByAuthor(firstName, lastName): 
	print firstName, lastName

def getRandomTextId(): 
	BASE_URL = 'https://www.gutenberg.org'
	letter = random.choice(string.ascii_letters)
	menuUrl = 'http://www.gutenberg.org/browse/authors/'+letter

	try: 
		html = urllib2.urlopen(menuUrl).read()
		soup = BeautifulSoup(html, "lxml")
		body = soup.find('div', {'class':'pgdbbyauthor'})
		authors = body.findAll('h2')
		names = [li.a["href"] for li in body.findAll('li', {"class": 'pgdbetext'})]
		book = random.choice(names).split("/ebooks/").pop()
		return book

	except urllib2.HTTPError as err:
		print "Page not found!"
		return getRandomTextId()
		if err.code == 404:
			print "Page not found!"


def getRandomText():
	bookId = getRandomTextId()
	print ("here", type(bookId))
	
	url = "http://www.gutenberg.org/cache/epub/"+bookId+"/pg"+bookId+".txt"
	text = None
	try: 
		html = urllib2.urlopen(url).read()
		soup = BeautifulSoup(html, "lxml")
		text = soup.find("p").getText().split("End of the Project")[0]

	except urllib2.HTTPError as err:
		print err
		if err.code == 404:
			print "Page not found!"
		elif err.code == 403:
			print ("Access denied!")
		else:
			print "Something happened! Error code", err.code

	except urllib2.URLError, err:
		print "Some other error happened:", err.reason
		
	if (text == None):
		text = readFile("timeMachine.txt").split("End of the Project")[0];
		text = text.split("End of the Project")[0];
		text = text.split("End of Project")[0]
	
	return text
	#http://www.gutenberg.org/cache/epub/





# https://automatetheboringstuff.com/chapter11/