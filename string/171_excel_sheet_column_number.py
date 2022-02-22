class Solution:
    # O(n) time | O(1) space - where n is the length of the string
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for char in columnTitle:
            res = res * 26 + ord(char) - ord('A') + 1
        return res
    