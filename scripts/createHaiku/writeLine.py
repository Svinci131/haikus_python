import random
from random import randint
from syllableCounting import getSyllables 

def getNextState(currState):
	nextState = random.choice(currState['possibilities'])
	return nextState
	# possibilities = state.keys()
	# for key, value in currState.items():
		

# # (num, dictionary) => string, line of that many syllables 
def writeLine (numOfSylbs, data): 
	remainingSylbs = numOfSylbs
	end = len(data.keys())
	currState = random.choice(data.keys()); 
	line = ""
	while(remainingSylbs > 0):
		line += (currState+" ");
		state = data[currState]; 
		nextState = getNextState(state)
		currState = nextState;
		remainingSylbs-=1

	print line
	return line

