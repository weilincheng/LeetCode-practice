class Solution:
    # O(n^2) time | O(n) space - where n is points.length
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 1
        result = 1
        for i in range(n):
            count = collections.defaultdict(int)
            p1 = points[i]
            for j in range(i + 1, n):
                p2, slope = points[j], float('inf')
                if p2[0] != p1[0]:
                    slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
                count[slope] += 1
                result = max(result, count[slope] + 1)
        return result

