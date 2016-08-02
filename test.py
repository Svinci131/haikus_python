from syllableCounting import getSyllables 

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
	}

	for key, value in tests.items():
		sylables = getSyllables(key)
		if (sylables != value):
			print (key, sylables, value)
