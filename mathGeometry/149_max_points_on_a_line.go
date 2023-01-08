func maxPoints(points [][]int) int {
    res := 1
    for i := 0; i < len(points); i++ {
        count := make(map[float64]int)
        p1 := points[i]
        for j := i + 1; j < len(points); j++ {
            p2 := points[j]
            slope := math.Inf(1)
            if p1[0] != p2[0] {
                slope = float64(p2[1] - p1[1]) / float64(p2[0] - p1[0])
            }
            count[slope]++
            res = int(math.Max(float64(res), float64(count[slope] + 1)))
        }
    }
    return res
}
