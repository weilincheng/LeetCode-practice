class Solution:
    # O(1) time | O(1) space since the number of row is fixed at 100.
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0] * k for k in range(1, 102)]
        dp[0][0] = poured
        for r in range(query_row + 1):
            for c in range(r + 1):
                if dp[r][c] > 1:
                    dp[r + 1][c] += (dp[r][c] - 1) / 2
                    dp[r + 1][c + 1] += (dp[r][c] - 1) / 2
                    
        return min(1, dp[query_row][query_glass])
    