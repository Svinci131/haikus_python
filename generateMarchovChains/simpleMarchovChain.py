# (str) => list of words
import os
import re
import string

def flattenLines(text):
	text = text.split("\n")
	content = ""
	for fragment in text: 
		if (fragment != ""):
			content+=(" "+(fragment))
	return content

def readFile (fileName):
	dirpath = os.path.relpath('../textFiles')
	fpath = os.path.join(dirpath, fileName)
	f = open(fpath)
	content = f.read().split('End of Project Gutenberg')[0]
	return flattenLines(content)

def calProbability (state): 
	transitions = len(state.keys())

# calculate the probability value by multiplying the probabilities in dict. 
# In this case probability of all state transition is

def generateMarchovChain():
	# parse text
	corpus = readFile("timeMachine.txt").lower();
	corpus = corpus.translate(string.maketrans("",""), string.punctuation)
	corpus = corpus.split();
	# parse text
	last = len(corpus)-1
	chain = {}
	for index, word in enumerate(corpus): 
		if (index != last):
			Next = corpus[(index+1)]
			state = {}
			if word in chain:
				state = chain[word]
				if Next in state:
					state[Next] += 1
				else:
					state[Next] = 1
			else: 
				state[Next] = 1
				chain[word] = state

	return chain

# def calcProbabilities():
# corpus = readFile("timeMachine.txt").lower();
# corpus = corpus.translate(string.maketrans("",""), string.punctuation)
# corpus = corpus.split();
chain =  generateMarchovChain()
print chain





