class Solution:
    # O(32) time | O(1) space 
    def findComplement(self, num: int) -> int:
        mask = ~0
        while mask & num > 0:
            mask <<= 1
        return mask ^ ~num
    