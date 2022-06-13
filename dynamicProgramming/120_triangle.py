class Solution:
    # O(n^2) time | O(n) space - where n is the length of the triangle
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0 for _ in range(len(triangle) + 1)]
        
        for row in triangle[::-1]:
            for idx, curVal in enumerate(row):
                dp[idx] = curVal + min(dp[idx], dp[idx + 1])
        
        return dp[0]
        
