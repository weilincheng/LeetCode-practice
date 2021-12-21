class Solution:
    # O(1) time | O(1) space 
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and not (n & n - 1)
