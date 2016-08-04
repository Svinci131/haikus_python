import random
import string
import webbrowser

def randomlyGetAuthor(): 
	letter = random.choice(string.ascii_letters)
	menuUrl = 'https://www.gutenberg.org/browse/authors/'+letter
	webbrowser.open(menuUrl)

randomlyGetAuthor()
# https://automatetheboringstuff.com/chapter11/