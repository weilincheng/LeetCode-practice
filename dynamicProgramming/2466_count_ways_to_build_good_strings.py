class Solution:
    # O(high) time | O(high) space 
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1
        MOD = 10 ** 9 + 7
        res = 0
        
        for i in range(1, high + 1):
            if i >= zero:
                dp[i] += dp[i - zero] % MOD
            if i >= one:
                dp[i] += dp[i - one] % MOD
            if i >= low:
                res += dp[i] % MOD
        
        return res % MOD

