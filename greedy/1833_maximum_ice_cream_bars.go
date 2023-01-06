func maxIceCream(costs []int, coins int) int {
    sort.Ints(costs)
    for idx, cost := range costs {
        coins -= cost
        if coins < 0 {
            return idx
        }
    }
    return len(costs)
}
