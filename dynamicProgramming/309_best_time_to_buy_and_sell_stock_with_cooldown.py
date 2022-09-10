class Solution:
    # O(n) time | O(n) space - where n is the length of the input array
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}
        
        def dfs(i, canBuy):
            if i >= len(prices):
                return 0
            if (i, canBuy) in cache:
                return cache[(i, canBuy)]
            
            cooldown = dfs(i + 1, canBuy)
            if canBuy:
                buy = dfs(i + 1, False) - prices[i]
                cache[(i, canBuy)] = max(cooldown, buy)
            else:
                sell = dfs(i + 2, True) + prices[i]
                cache[(i, canBuy)] = max(cooldown, sell)
            
            return cache[(i, canBuy)]
        
        return dfs(0, True)

