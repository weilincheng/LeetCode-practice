// O(log(n)) time | O(1) space 
func isUgly(n int) bool {
    if n <= 0 {
        return false
    }
    
    primeFactors := []int{2, 3, 5}
    for _, factor := range primeFactors {
        for n % factor == 0 {
            n /= factor
        }
    }
    return n == 1
}
