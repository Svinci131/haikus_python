import os
from syllableCounting import getSyllables 

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
	order = [5,7,5]; 
	testSyllables()
	# print (getSyllables('Ferret'), "should be 2")
	# print (getSyllables('about'), "should be 2"); 
	# print (getSyllables('shoe'), "should be 1"); 
	# print (getSyllables('Boy'), "should be 1"); 
	# print (getSyllables('lynx'),"should be 1");
	# print (getSyllables('happy'),"should be 2");
	# print (getSyllables('preserve'), "sould be two");
	# print (getSyllables('resevior'), "should be 3"); 
	# print (getSyllables("engagement"), "should be 3")
	# for word in data:
	# 	getSyllables(word)

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

