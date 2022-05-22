class Solution:
    # O(n^2) time | O(1) space 
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += self.countPalindrom(s, i, i)
            res += self.countPalindrom(s, i, i + 1)
        
        return res

    def countPalindrom(self, s, l, r):
        ans = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            ans += 1
            l, r = l - 1, r + 1
        return ans