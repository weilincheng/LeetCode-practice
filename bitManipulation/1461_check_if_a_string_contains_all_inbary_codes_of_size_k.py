class Solution:
    # O(n*k) time | O(n*k) space - where n is the length of string
    def hasAllCodes(self, s: str, k: int) -> bool:
        uniqueCode = set()
        for i in range(len(s) - k + 1):
            curCode = s[i : i + k]
            uniqueCode.add(curCode)
        return len(uniqueCode) == 2 ** k

