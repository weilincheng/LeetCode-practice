class Solution:
    # O(n) time | O(1) space - where n is the length of the input array
    def reverseString(self, s: List[str]) -> None:
        lIdx = 0
        rIdx = len(s) - 1
        
        while lIdx < rIdx:
            s[lIdx], s[rIdx] = s[rIdx], s[lIdx]
            lIdx, rIdx = lIdx + 1, rIdx - 1