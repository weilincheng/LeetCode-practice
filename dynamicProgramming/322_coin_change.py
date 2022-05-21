class Solution:
    # O(m * n) time | O(m) space - where m is the amount and n is the coins.length
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        dp = [float('inf') for k in range(amount + 1)]
        dp[0] = 0
        
        for a in range(1, amount + 1):
            for coin in coins:
                if a - coin >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - coin])
                    
        return -1 if dp[amount] == float(inf) else dp[amount]
