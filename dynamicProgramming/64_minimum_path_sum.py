class Solution:
    # O(m*n) time | O(n) spcae
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        dp = [float('inf') for _ in range(COLS + 1)]
        
        for r in range(ROWS - 1, -1, -1):
            nextDP = [float('inf') for _ in range(COLS + 1)]
            for c in range(COLS - 1, -1, -1):
                nextDP[c] = grid[r][c] 
                if r == ROWS - 1 and c == COLS - 1: continue
                nextDP[c] += min(dp[c], nextDP[c + 1])
            dp = nextDP
                
        return dp[0]

