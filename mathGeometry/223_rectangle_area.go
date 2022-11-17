func computeArea(ax1 int, ay1 int, ax2 int, ay2 int, bx1 int, by1 int, bx2 int, by2 int) int {
    xOverlap := int(math.Min(float64(ax2), float64(bx2)) - math.Max(float64(ax1), float64(bx1)))
    yOverlap := int(math.Min(float64(ay2), float64(by2)) - math.Max(float64(ay1), float64(by1)))
    totalArea := (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1)
    
    if xOverlap > 0 && yOverlap > 0 {
        return totalArea - xOverlap * yOverlap
    }
    return totalArea
}
