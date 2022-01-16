class Solution:
    # O(n) time | O(n) space 
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0 for i in range(n + 1)]
        for i in range(n - 1, -1, -1):
            point, brainPower = questions[i]
            dp[i] = max(dp[i + 1], point + dp[min(n, i + brainPower + 1)])
        return dp[0]
    