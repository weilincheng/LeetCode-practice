class Solution:
    # O(n) time | O(1) space - where n is the length of the input array
    def moveZeroes(self, nums: List[int]) -> None:
        lastZeroIdx = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastZeroIdx] = nums[i]
                lastZeroIdx += 1
                
        for i in range(lastZeroIdx, len(nums)):
            nums[i] = 0