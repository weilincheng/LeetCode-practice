class Solution:
    # O(n) time | O(1) space - where n is the lenght of input ops 
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m * n
        minA, minB = m, n 
        for op in ops:
            minA = min(minA, op[0])
            minB = min(minB, op[1])
        return minA * minB
    