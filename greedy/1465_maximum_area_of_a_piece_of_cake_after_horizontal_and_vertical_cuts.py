class Solution:
    # O(n) time | O(n) space - where n is the length of input arrays
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        hCutMax = max(h - horizontalCuts[-1], horizontalCuts[0])
        vCutMax = max(w - verticalCuts[-1], verticalCuts[0])
        for i in range(len(horizontalCuts) - 1):
            cut = horizontalCuts[i + 1] - horizontalCuts[i]
            hCutMax = max(cut, hCutMax)
        for i in range(len(verticalCuts) - 1):
            cut = verticalCuts[i + 1] - verticalCuts[i]
            vCutMax = max(cut, vCutMax)
            
        return hCutMax * vCutMax % (10**9 + 7)

