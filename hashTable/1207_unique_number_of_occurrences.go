// O(n) time | O(n) space - where n is the length of the input array
func uniqueOccurrences(arr []int) bool {
    freq := make(map[int]int)
    for _, val := range arr {
        freq[val]++
    }
    seenFreq := make(map[int]bool)
    for _, v := range freq {
        if _, exist := seenFreq[v]; exist {
            return false
        }
        seenFreq[v] = true
    }
    return true
}
