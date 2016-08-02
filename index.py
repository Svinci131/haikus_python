import os
from syllableCounting import getSyllables 
from random import randint


def testSyllables():
	tests = {
		'Ferret': 2, 
		'about': 2, 
		'shoe': 1, 
		'Boy': 1, 
		'lynx':1,
		'happy':2,
		'preserve': 2,
		'perseverance': 4,
		'resevior': 3, 
		"engagement": 3,
		"data": 2,
	}

	for key, value in tests.items():
		sylables = getSyllables(key)
		if (sylables != value):
			print (key, sylables, value)

# (list of words) => haiku as str
def createHaiku(data):
	haiku = "";
	lines = [5,7,5]; 

	for line in lines: 
		haiku += writeLine(line, data)

	print haiku

# (num, list) => string, line of that many syllables 
def writeLine (numOfSylbs, data): 
	remainingSylbs = numOfSylbs
	end = len(data)-1;
	start = randint(0, end)
	line = ""

	while(remainingSylbs > 0):
		for i in range(start, end):
			word = data[i]
			sylbCount = getSyllables(word)
			if sylbCount <= remainingSylbs:

				if len(line) == 0: 
					line += word
				else:
					line += (" "+word)

				remainingSylbs -= sylbCount
				if (remainingSylbs == 0):
					break;
	return line+"\n"

# (str) => list of words
def readFile (fileName):
	dirpath = os.path.relpath('textFiles')
	fpath = os.path.join(dirpath, fileName)
	f = open(fpath)
	content = f.read().split();
	return content

data = readFile("timeMachine.txt")
createHaiku(data)





# array vs list

