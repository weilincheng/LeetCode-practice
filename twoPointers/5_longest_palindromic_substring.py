class Solution:
    # O(n^2) time | O(1) space - where n is the length of the string
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(res):
                    res = s[left : right + 1] 
                left, right = left - 1, right + 1
        
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(res):
                    res = s[left : right + 1] 
                left, right = left - 1, right + 1
        return res

