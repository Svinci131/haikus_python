import random
from random import randint
from syllableCounting import getSyllables 

badStates = {}; 
line = []

#(list, int) => list
def getPossiblities(possibleStates, remainingSylbs):
	possibilities = []
	for key, value in possibleStates.items():
		#if ((key in badStates) != True):
		sylbs = getSyllables(key)
		if sylbs <= remainingSylbs: 
			for i in range(1, value):
				#{'val': key, 'sylbs': sylbs} d
				possibilities.append(key)
	return possibilities

def getRandomFirstState(sylbMax, data): 
	word = random.choice(data.keys());
	if (getSyllables(word) <= sylbMax): 
		return word; 
	else:
	 	return getRandomFirstState(sylbMax, data)

# # (num, dictionary) => string, line of that many syllables 
def writeLine (numOfSylbs, data, start): 
	remainingSylbs = numOfSylbs
	currState = getRandomFirstState(remainingSylbs, data) # or start
	#while there are syllables

	while(remainingSylbs > 0):
		# add the current state to line 
		sylbs = getSyllables(currState);
		remainingSylbs-=sylbs;
		line.append(currState);

		if (remainingSylbs > 0):
			possibilities = getPossiblities(data[currState], remainingSylbs)
			if ((len(possibilities)-1) <= 0): 
				line.pop();
				remainingSylbs+=getSyllables(currState)
				currState = getRandomFirstState(remainingSylbs, data)
			else:
				currState = random.choice(possibilities)
	
	return " ".join(line)
