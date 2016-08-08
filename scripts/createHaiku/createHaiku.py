# from simpleMarchovChain import generateMarchovChain
import sys
basePath = '/Users/samanthavinci/Desktop/literaryHaiku/scripts/'
from writeLine import writeLine
#markov chain tool
#takes a file name reads the text, formats corpus and generates Chain
sys.path.append(basePath+'markovChains')
from simpleMarkovChain import generateMarkovChain

# (filename) => haiku as str
def createHaiku(text):
	data = generateMarkovChain(text)
	haiku = "";
	lines = [5,7,5]; 
	# print writeLine(5, data)
	for i, line in enumerate(lines): 
		if i == 0: 
			haiku+=(writeLine(line, data, None)+"\n")
		else: 
			start = haiku.split().pop()
			haiku+=(writeLine(line, data, start)+"\n")
	print "-------"
	print haiku
	# print " ".join(writeLine(5, data, None))





# array vs list

