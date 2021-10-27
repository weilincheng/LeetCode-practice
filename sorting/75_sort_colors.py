class Solution:
    # O(n) time | O(1) space - where n is the length of the input array 
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start, end, index = 0, len(nums) - 1, 0
        
        while index <= end and start < end:
            if nums[index] == 0:
                nums[start], nums[index] = nums[index], nums[start]
                start += 1
                index += 1
            elif nums[index] == 2:
                nums[end], nums[index] = nums[index], nums[end]
                end -= 1
            else: 
                index += 1
    