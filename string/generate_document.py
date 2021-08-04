# O(n+m) time | O(c) space - where n is the number of characters, m is
# the length of the document, and c is the number of unique characters in the character string
def generateDocument(characters, document):
	characterCounts = {}
	for character in characters:
		if character in characterCounts:
			characterCounts[character] += 1
		else:
			characterCounts[character] = 1
	
	for character in document:
		if character not in characterCounts or characterCounts[character] == 0:
			return False
		else:
			characterCounts[character] -= 1
	
	return True
