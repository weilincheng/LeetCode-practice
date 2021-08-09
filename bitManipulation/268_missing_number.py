class Solution:
    # O(n) time | O(1) space where n is the length of the input array
    def missingNumber(self, nums: List[int]) -> int:
        missingNumber = 0
        for i in range(len(nums)):
            missingNumber ^= nums[i]
            
        for i in range(len(nums) + 1):
            missingNumber ^= i
        
        return missingNumber
    