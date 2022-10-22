func minWindow(s string, t string) string {
    countT, window := make(map[byte]int), make(map[byte]int)
    for i := range t {
        countT[t[i]]++
    }
    have, need := 0, len(countT)
    res, resLen := []int{-1, -1}, math.Inf(1)
    
    l := 0
    for r := range s {
        window[s[r]]++
        if count, exist := countT[s[r]]; exist && window[s[r]] == count {
            have++
        }
        
        for have == need {
            if float64(r - l + 1) < resLen {
                resLen = float64(r - l + 1)
                res = []int{l, r}
            }
            window[s[l]]--
            if count, exist := countT[s[l]]; exist && window[s[l]] < count {
                have--           
            }
            l++
        }
    }
    if float64(resLen) != math.Inf(1) {
        return s[res[0]:res[1]+1]
    }
    return ""
}
