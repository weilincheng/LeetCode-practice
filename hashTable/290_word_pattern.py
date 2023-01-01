class Solution:
    # O(m+n) time | O(m+n) space - where m is pattern.length and n is s.length
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        charToWord, wordToChar = {}, {}
        for char, word in zip(pattern, words):
            if (char in charToWord and charToWord[char] != word) or (word in wordToChar and wordToChar[word] != char):
                return False
            charToWord[char] = word
            wordToChar[word] = char
        return True

