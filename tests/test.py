# need to learn more abt correct python testing
# from syllableCounting import getSyllables 
import scripts
from createHaiku import createHaiku
#https://docs.python.org/3/tutorial/modules.html
print scripts

def testSyllables():
	tests = {
		'Ferret': 2, 
		'about': 2, 
		'shoe': 1, 
		'Boy': 1, 
		'lynx':1,
		'happy':2,
		'preserve': 2,
		'perseverance': 4,
		'resevior': 3, 
		"engagement": 3,
		"data": 2,
		"credible": 3,
		"orders": 2,
		"medium":3,
		"unemployed": 4, 
		"the":1
	}

	for key, value in tests.items():
		sylables = getSyllables(key)
		if (sylables != value):
			print (key, sylables, value)
