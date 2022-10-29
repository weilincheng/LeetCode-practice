class Solution:
    # O(nlog(n)) time | O(n) space - where n is the length of the input array
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        curPlantTime, res = 0, 0
        indices = sorted(range(len(plantTime)), key=lambda x: -growTime[x])
        for i in indices:
            curPlantTime += plantTime[i]
            res = max(res, curPlantTime + growTime[i])
        
        return res

