
import re
from readFile import readFile 

# Markov chain which will be represented as a python dictionary.
# storing the word that occurs after each bi-gram (two words) in a list that can be accessed using the bi-gram key
# I like cats I like dogs I dont like ferrets

def generateMarchovChain():
	corpus = readFile("timeMachine.txt")

	print corpus
