class Solution:
    # O(n) time | O(1) space - where n is the length of string
    def validPalindrome(self, s: str) -> bool:
        def isPalindrom(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True
        
        left, right, deleteLeft = 0, len(s) - 1, 1
        while left < right:
            if s[left] != s[right] and deleteLeft:
                return isPalindrom(left + 1, right) or isPalindrom(left, right - 1)
            left, right = left + 1, right - 1
        return True
    