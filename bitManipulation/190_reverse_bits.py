class Solution:
    # O(32) time | O(1) space
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            lastDigit = n & 1
            n >>= 1
            res |= lastDigit << (31 - i)
        return res
    
