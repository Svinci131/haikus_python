from sys import version_info
from createHaiku import createHaiku 
from scraper import getRandomText
from getDefaultText import getDefaultText

py3 = version_info[0] > 2 #creates boolean value for test that Python major version > 2

prompt = "Press 1 to use author press 2 to generate random"

if py3:
	selection = input(prompt)
else:
	selection = raw_input(prompt)

if selection =='1': 
	print "This feature is coming soon"

elif selection == '2':
	text = getDefaultText()
	# text = getRandomText()
	createHaiku(text)

else:
	print "Unknown Option Selected!" 


# createHaiku("timeMachine.text")

