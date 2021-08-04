class Solution:
    # O(n) time | O(1) space
    def firstUniqChar(self, s: str) -> int:
        charCounts = {}
        
        for char in s:
            if char not in charCounts:
                charCounts[char] = 0
                
            charCounts[char] += 1
        
        for i in range(len(s)):
            if charCounts[s[i]] == 1:
                return i
        
        return -1