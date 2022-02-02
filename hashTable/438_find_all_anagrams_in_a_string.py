class Solution:
    # O(n) time | O(1) space - where n is the length of the s string
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []
        pCount, sCount = {}, {}
        for i in range(len(p)):
            pCount[p[i]] = pCount.get(p[i], 0) + 1
            sCount[s[i]] = sCount.get(s[i], 0) + 1

        result = [0] if pCount == sCount else []
        
        l = 0 
        for r in range(len(p), len(s)):
            sCount[s[l]] -= 1
            if sCount[s[l]] == 0:
                sCount.pop(s[l])
            sCount[s[r]] = sCount.get(s[r], 0) + 1
            l += 1
            if sCount == pCount:
                result.append(l)
        return result 
    