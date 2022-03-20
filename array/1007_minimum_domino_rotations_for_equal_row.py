class Solution:
    # O(2n) time | O(1) space - where n is the length of the array
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        for target in [tops[0], bottoms[0]]:
            t, b = 0, 0
            for i in range(n):
                if tops[i] != target and bottoms[i] != target:
                    break
                if tops[i] != target: t += 1
                if bottoms[i] != target: b += 1
                if i == n - 1: 
                    return min(t, b)
        return -1
    