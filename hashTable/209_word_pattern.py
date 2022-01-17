class Solution:
    # O(n) tim | O(n) space - where n is the length of the pattern
    def wordPattern(self, pattern: str, s: str) -> bool:
        charMap, seenWord, words = {}, set(), s.split()
        if len(pattern) != len(words): return False
        
        for char, word in zip(pattern, words):
            if char in charMap:
                if charMap[char] != word: return False
            else:
                if word in seenWord: return False
                charMap[char] = word
                seenWord.add(word)
        return True
