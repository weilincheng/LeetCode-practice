class Solution:
    # O(n^2) time | O(n) space 
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res = []
        people.sort(key = lambda k : (-k[0], k[1]))
        for p in people:
            res.insert(p[1], p)
        return res
    
