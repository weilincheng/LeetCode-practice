class Solution:
    # O(n) time | O(1) space - where n is the len of array
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted = True
        minVal, maxVal = float('inf'), float('-inf')
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                sorted = False
            if not sorted:
                minVal = min(minVal, nums[i])
        
        sorted = True
        for i in reversed(range(len(nums) - 1)):
            if nums[i] > nums[i + 1]:
                sorted = False
            if not sorted:
                maxVal = max(maxVal, nums[i])
        
        start, end = 0, len(nums) - 1
        for i in range(len(nums)):
            if nums[i] > minVal:
                break
            start += 1
        
        for i in reversed(range(len(nums))):
            if nums[i] < maxVal:
                break
            end -= 1
            
        return 0 if end - start < 0 else end - start + 1
