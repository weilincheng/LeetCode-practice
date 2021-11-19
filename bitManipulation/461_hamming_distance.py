class Solution:
    # O(n) time | O(1) space - where n is the number of bits to represent x^y
    def hammingDistance(self, x: int, y: int) -> int:
        xor, differentBit = bin(x ^ y), 0     
        for bit in xor:
            if bit == "1":
                differentBit += 1
        return differentBit
