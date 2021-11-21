class Solution:
    # O(n^2) time | O(1) space - where n is the length of the input array
    def maxDistance(self, colors: List[int]) -> int:
        maxDist = 0
        for i in range(len(colors)):
            for j in range(i, len(colors)):
                if colors[i] != colors[j]:
                    maxDist = max(maxDist, j - i)
        return maxDist
