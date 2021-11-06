class Solution:
    # O(n) time | O(1) space 
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0 
        for num in nums:
            xor ^= num
        rightmost1Bit = 1
        while xor & rightmost1Bit == 0:
            rightmost1Bit <<= 1
        
        res = [0, 0]
        for num in nums:
            if num & rightmost1Bit:
                res[0] ^= num
            else:
                res[1] ^= num
        return res
    