class Solution:
    # O(nlogn) time | O(n) space 
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        right = points[0][1]
        arrow = 1
        for i in range(1, len(points)):
            start, end = points[i]
            if start > right: 
                arrow += 1
                right = end
        return arrow
    