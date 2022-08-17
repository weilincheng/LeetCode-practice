class Solution:
    # O(n) time | O(n) space - where n is the length of the input array
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morseCodeMap = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        wordSet = set()
        
        for word in words:
            morseCode = []
            for c in word:
                curCode = morseCodeMap[ord(c) - ord('a')]
                morseCode.append(curCode)
            wordSet.add("".join(morseCode))
        
        return len(wordSet)
    
