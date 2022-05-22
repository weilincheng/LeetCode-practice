class Solution:
    # O(n^2) time | O(1) space 
    def countSubstrings(self, s: str) -> int:
        def checkLeftRight(l, r):
            ans = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                ans += 1
                l, r = l - 1, r + 1
            return ans
        
        res = 0
        for i in range(len(s)):
            l = r = i
            res += checkLeftRight(l, r)
            
            l, r = i, i + 1
            res += checkLeftRight(l, r)
        
        return res
