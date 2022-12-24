// O(n) time | O(n) space
func numTilings(n int) int {
    MOD := int(math.Pow(10, 9) + 7)
    dp := make([][]int, n + 1)
    for i := range dp {
        dp[i] = make([]int, 2)
        for j := range dp[i] {
            dp[i][j] = 0
        }
    }
    dp[0][0], dp[1][0] = 1, 1
    for i := 2; i <= n; i++ {
        dp[i][0] = (dp[i-1][0] + dp[i-2][0] + dp[i-1][1] * 2) % MOD
        dp[i][1] = (dp[i-2][0] + dp[i-1][1]) % MOD
    }
    return dp[n][0]
}

