// O(n) time | O(n) space - where n is prices.length
func maxProfit(prices []int) int {
    dp := make(map[string]int)
    return dfs(0, true, prices, dp)
}

func dfs(i int, buying bool, prices []int, dp map[string]int) int {
    if i >= len(prices) {
        return 0
    }
    key := strconv.Itoa(i) + "-" + strconv.FormatBool(buying)
    if profit, ok := dp[key]; ok {
        return profit
    }

    cooldown := dfs(i+1, buying, prices, dp)
    if buying {
        buy := dfs(i+1, !buying, prices, dp) - prices[i]
        dp[key] = int(math.Max(float64(buy), float64(cooldown)))
    } else {
        sell := dfs(i+2, !buying, prices, dp) + prices[i]
        dp[key] = int(math.Max(float64(sell), float64(cooldown)))
    }
    return dp[key]
}
