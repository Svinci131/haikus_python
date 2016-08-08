# (str) => list of words
import re
import string

#BUG DIDNT ADD IF IT REPEATS
def generateMarkovChain(text):
	# parse text
	corpus = text.lower()
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
					state[Next]+= 1
				else: 
					state[Next] = 1
				#state['possibilities'].append(Next)
			else:
				#state['possibilities'] = []
				#state['possibilities'].append(Next)
				state[Next] = 1
				chain[word] = state


	return chain

# def calcProbabilities():
# corpus = readFile("timeMachine.txt").lower();
# corpus = corpus.translate(string.maketrans("",""), string.punctuation)
# corpus = corpus.split();



# def calProbability (state): 
# 	transitions = len(state.keys())

# calculate the probability value by multiplying the probabilities in dict. 
# In this case probability of all state transition is





