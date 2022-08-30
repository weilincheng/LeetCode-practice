class Solution:
    # O(k) time | O(1) space 
    def smallestRepunitDivByK(self, k: int) -> int:
        remainder = 0 
        for length in range(1, k + 1):
            remainder = (remainder * 10 + 1) % k
            if remainder % k == 0:
                return length
        
        return -1
            