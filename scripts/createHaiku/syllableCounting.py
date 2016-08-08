# (str) => boolean - O(1)
def isVowel(letter, i):
	if letter == "y" and (i == 0):
		return True 
	if letter in ('a', 'e', 'i', 'o', 'u', 'y'):
		return True;
	else: 
		return False

# (str) => num
def getSyllables(string):
	syllables = 0
	letters = list(string.lower());
	last = len(letters)-1;
	vowelCount = 0; 
	if (len(string) == 1): 
		return 1

	for index, letter in enumerate(letters):
		prev = letters[(index-1)]; 
		if (isVowel(letter, index)):
			vowelCount+=1
		# if a cosnant is proceeded by a val add a syllable
		if (isVowel(letter, index) == False and isVowel(prev, index) == True): 
			syllables+=1

		if (letter == "u" and prev == "i"):
			syllables+=1
		# if the last letter is a "e"
		if (index == last and letter == 'e' and isVowel(prev, index) == False):
			
			if (vowelCount > 1): 
				#handle, ladle, credible
				if (prev != "l"):
					syllables-=1

		
	return syllables


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
		"the":1,
		"at":1,
		"I":1
	}

	for key, value in tests.items():
		sylables = getSyllables(key)
		if (sylables != value):
			print (key, sylables, value)

#
