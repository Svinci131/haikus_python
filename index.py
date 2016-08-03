from readFile import readFile 
from syllableCounting import getSyllables 
import random
from random import randint
from simpleMarchovChain import generateMarchovChain
# (list of words) => haiku as str

def createHaiku(fileName):
	data = generateMarchovChain()
	haiku = "";
	lines = [5,7,5]; 

	for line in lines: 
		writeLine(line, data)

# 	print haiku

# # (num, list) => string, line of that many syllables 
def writeLine (numOfSylbs, data): 
	remainingSylbs = numOfSylbs
	end = len(data.keys())
	currState = random.choice(data.keys()); 
	line = ""
	while(remainingSylbs > 0):
		line += (currState+" ");
		state = data[currState]; 
		nextState = state.keys()[0]
		currState = nextState;
		remainingSylbs-=1
	print (line);
# 	line = ""

# 	while(remainingSylbs > 0):
# 		for i in range(start, end):
# 			word = data[i]
# 			sylbCount = getSyllables(word)
# 			if sylbCount <= remainingSylbs:

# 				if len(line) == 0: 
# 					line += word
# 				else:
# 					line += (" "+word)

# 				remainingSylbs -= sylbCount
# 				if (remainingSylbs == 0):
# 					break;
# 	return line+"\n"




createHaiku("timeMachine.txt")





# array vs list

