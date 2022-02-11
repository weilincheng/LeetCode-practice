class Solution:
    # O(n) time | O(1) space - where n is the length of the input string
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        s1Count, s2Count = [0 for _ in range(26)], [0 for _ in range(26)]
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1 
        
        matches = 0
        for i in range(26):
            if s1Count[i] == s2Count[i]: matches += 1
        l, r = 0, len(s1)
        while r < len(s2):
            if matches == 26: return True
            
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] == s2Count[index] + 1:
                matches -= 1
            
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] == s2Count[index] - 1:
                matches -= 1           
            l, r = l + 1, r + 1
            
        return matches == 26
