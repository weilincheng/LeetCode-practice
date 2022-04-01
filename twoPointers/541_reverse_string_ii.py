class Solution:
    # O(n) time | O(n) space - where n is the length of s
    def reverseStr(self, s: str, k: int) -> str:
        a = list(s)
        for i in range(0, len(a), 2 * k):
            a[i:i+k] = reversed(a[i:i+k])
        return "".join(a)
    