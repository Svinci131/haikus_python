import os
from syllableCounting import getSyllables 

# (list of words) => haiku as str
def createHaiku(data):
	haiku = "";
	order = [5,7,5]; 
	for word in data:
		getSyllables(word)

# (str) => list of words
# def readFile (fileName):
dirpath = os.path.relpath('textFiles')
fpath = os.path.join(dirpath, "timeMachine.txt")
f = open(fpath)
content = f.read().split();
createHaiku(content)





# array vs list

