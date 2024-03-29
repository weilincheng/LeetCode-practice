// O(m*n) time | O(m*n) space - where m is text1.length and n is text2.length
func longestCommonSubsequence(text1 string, text2 string) int {
    dp := make([][]int, len(text1) + 1)
    for i := range dp {
        dp[i] = make([]int, len(text2) + 1)
    }

    for i := 0; i < len(text1); i++ {
        for j := 0; j < len(text2); j++ {
            dp[i][j] = 0
        }   
    }

    for i := len(text1) - 1; i >= 0; i-- {
        for j := len(text2) - 1; j >= 0; j-- {
            if text1[i] == text2[j] {
                dp[i][j] = 1 + dp[i + 1][j + 1]
            } else {
                dp[i][j] = int(math.Max(float64(dp[i + 1][j]), float64(dp[i][j + 1])))
            }
        }
    }

    return dp[0][0]
}

