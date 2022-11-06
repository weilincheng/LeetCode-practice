class Solution:
    # O(n^2) time | O(n) space - where n is the length of s
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            return min(s[i:] + s[:i] for i in range(len(s)))
        
        return "".join(sorted(s))

