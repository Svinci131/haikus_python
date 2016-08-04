# from simpleMarchovChain import generateMarchovChain
import sys
basePath = '/Users/samanthavinci/Desktop/literaryHaiku/scripts/'
from writeLine import writeLine
#markov chain tool
#takes a file name reads the text, formats corpus and generates Chain
sys.path.append(basePath+'markovChains')
from simpleMarkovChain import generateMarkovChain

# (filename) => haiku as str
def createHaiku(fileName):
	data = generateMarkovChain()
	haiku = "";
	lines = [5,7,5]; 
	# print writeLine(5, data)
	for line in lines: 
		writeLine(line, data)

	print haiku








# array vs list

