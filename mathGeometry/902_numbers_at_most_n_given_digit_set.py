class Solution:
    # O(log10(n)) time | O(1) space
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        s = str(n)
        n = len(s)
        # Less than k digits
        ans = sum(len(digits) ** i for i in range(1, n))
        
        # k digits
        for i, c in enumerate(s):
            ans += len(digits) ** (n - i - 1) * sum(d < c for d in digits)
            if c not in digits: return ans
        return ans + 1
    