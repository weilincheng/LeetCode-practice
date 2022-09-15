class Solution:
    # O(nlog(n)) time | O(n) space - where n is the length of the input array
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        N = len(changed)
        if N % 2 == 1: return []
        numFreq = Counter(changed)
        res = []
        
        for num in sorted(changed):
            if numFreq[num] == 0: continue
            elif numFreq[num * 2] == 0: return []
            elif num == 0 and numFreq[num] == 0: return []
            numFreq[num] -= 1
            numFreq[num * 2] -= 1
            res.append(num)
        
        return res 

