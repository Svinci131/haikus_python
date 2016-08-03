import os
import sys
import nltk
import nltk.data
from nltk.tokenize import sent_tokenize, word_tokenize
import re

# nltk.download()
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
	#get rid of line breaks
	text = flattenLines(text)
	#split along sentances
	text = sent_tokenize(text)
	return text

def parseText(text):
	corpus = text.lower();
	corpus = corpus.translate(string.maketrans("",""), string.punctuation)
	corpus = corpus.split();

# (str) => list of words
def readFile (fileName):
	basepath = os.path.dirname(__file__)
	fpath = os.path.abspath(os.path.join(basepath, "..", "../textFiles", fileName))
	 # dirpath = os.path.relpath('../../textFiles')
	 # fpath = os.path.join(dirpath, fileName)
	f = open(fpath)
	content = f.read()
	# content = formatText(content)
	return content



