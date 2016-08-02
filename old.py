from readFile import readFile 
from syllableCounting import getSyllables 
from random import randint

# (list of words) => haiku as str
def createHaiku(fileName):
	data = readFile(fileName).split();
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




createHaiku("timeMachine.txt")





# array vs list

