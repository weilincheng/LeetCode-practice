class Solution:
    # O(n) time | O(1) space - where n is cardPoints.length
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        totalSum = sum(cardPoints)
        N = len(cardPoints)
        size = N - k
        subSum = minSum = sum(cardPoints[:size])
        for i in range(size, N):
            subSum += cardPoints[i] - cardPoints[i - size]
            minSum = min(minSum, subSum)
        return totalSum - minSum

