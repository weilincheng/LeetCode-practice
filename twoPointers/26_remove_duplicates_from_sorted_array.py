class Solution:
    # O(n) time | O(1) space - where n is nums.length
    def removeDuplicates(self, nums: List[int]) -> int:
        insertIdx = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[insertIdx] = nums[i]
                insertIdx += 1
        
        return insertIdx

