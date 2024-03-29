class Solution:
    # O(n) time | O(1) space - where n is the length of the input array
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup, missing = -1, 1
        
        for num in nums:
            if nums[abs(num) - 1] < 0:
                dup = abs(num)
            else:
                nums[abs(num) - 1] *= -1
        
        for i in range(1, len(nums)):
            if nums[i] > 0:
                missing = i + 1
                break
        return [dup, missing]

