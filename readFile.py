import os
import nltk
import nltk.data
from nltk.tokenize import sent_tokenize, word_tokenize
import re

nltk.download()
def flattenLines(text):
	text = text.split("\n")
	content = ""
	for fragment in text: 
		if (fragment != ""):
			content+=(" "+(fragment))
	return content

def formatText(text):
	#remove end default text
	text = text.split('End of Project Gutenberg')[0]
	text = flattenLines(text)
	text = sent_tokenize(text)
	#text = re.split("\/(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s", text)
	return text


# (str) => list of words
def readFile (fileName):
	dirpath = os.path.relpath('textFiles')
	fpath = os.path.join(dirpath, fileName)
	f = open(fpath)
	content = f.read()
	content = formatText(content)
	return content