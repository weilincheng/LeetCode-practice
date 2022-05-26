class Solution:
    # O(1) time | O(1) space - where the input binary string length is 32 at most 
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= (n - 1)
            count += 1
        return count
    