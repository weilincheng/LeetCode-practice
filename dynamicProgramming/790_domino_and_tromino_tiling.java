class Solution {
    // O(n) time | O(n) space
    public int numTilings(int n) {
        final long MOD = 1000000007;
        long[][] dp = new long[n+1][2];
        dp[0][0] = dp[1][0] = 1;
        for (int i = 2; i <= n; i++) {
            dp[i][0] = (dp[i-1][0] + dp[i-2][0] + dp[i-1][1] * 2) % MOD;
            dp[i][1] = (dp[i-2][0] + dp[i-1][1]) % MOD;
        }
        return (int)dp[n][0];
    }
}
