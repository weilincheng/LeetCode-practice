class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = s.replace(' ','').lower()
        t = t.replace(' ','').lower()

        # Edge Case Check
        if len(s) != len(t):
            return False
        
        count = {}

        for letter in s:
            if letter in count:
                count[letter] += 1
            else:
                count[letter] = 1
                
        for letter in t:
            if letter in count:
                count[letter] -= 1
            else: 
                count[letter] = 1
            
        for letter in count:
            if count[letter] >= 1:
                return False
        
        return True