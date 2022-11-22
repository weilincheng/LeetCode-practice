class Solution:
    # O(n * sqrt(n)) time | O(n) space
    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1)
        dp[0] = 0
        squares = []
        for i in range(1, n + 1):
            square = i ** 2
            if square > n: break
            squares.append(square) 
        
        for target in range(1, n + 1):
            for square in squares:
                if square > target: break        
                dp[target] = min(dp[target], 1 + dp[target - square])
        
        return dp[n]
    
