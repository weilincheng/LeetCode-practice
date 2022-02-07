class Solution:
    # O(n) time | O(1) space - where n is the length of the input string
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0
        for char in s:
            result ^= ord(char)
        for char in t:
            result ^= ord(char)
        return chr(result)
    