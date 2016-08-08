import sys
basePath = '/Users/samanthavinci/Desktop/literaryHaiku/scripts/'
sys.path.append(basePath+'readFile')
from readFile import readFile 

def getDefaultText ():
	text = readFile("timeMachine.txt").split("End of the Project")[0];
	text = text.split("End of the Project")[0];
	text = text.split("End of Project")[0]
	return text

