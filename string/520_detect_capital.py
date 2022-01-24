class Solution:
    # O(n) time | O(1) space 
    def detectCapitalUse(self, word: str) -> bool:
        return word.islower() or word.isupper() or word.istitle()
