// O(n) time | O(n) space - where n is temperatures.length
func dailyTemperatures(temperatures []int) []int {
    ans := make([]int, len(temperatures))
    for i := range ans {
        ans[i] = 0
    }

    stack := []int{}
    for idx, temp := range temperatures {
        for len(stack) > 0 && temp > temperatures[stack[len(stack) - 1]] {
            prevIdx := stack[len(stack) - 1]
            stack = stack[:len(stack) - 1]
            ans[prevIdx] = idx - prevIdx
        }
        stack = append(stack, idx)
    }
    return ans
}
