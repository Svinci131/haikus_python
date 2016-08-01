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

	for index, letter in enumerate(letters):
		prev = letters[(index-1)]; 

		# if a cosnant is proceeded by a val add a syllable
		if (isVowel(letter, index) == False and isVowel(prev, index) == True): 
			syllables+=1

		# if the last letter is a "e"
		if (index == last and letter == 'e' and isVowel(prev, index) == False): 
			syllables-=1
		
	return syllables

# ('preserve', 3, 2)
# ('engagement', 4, 3)
# ('lynx', 0, 1)
# ('happy', 1, 2)
	#get all vowels that aren't the last letter and aren't next to another vowel
	#your, he, quiet, boy, lynx, happy, preserve, resevior 
