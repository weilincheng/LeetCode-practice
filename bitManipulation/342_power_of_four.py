class Solution:
    # O(1) time | O(1) space 
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0 and int(sqrt(n)) * int(sqrt(n)) == n

