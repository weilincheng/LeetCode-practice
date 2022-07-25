class Solution:
    # O(log(n)) time | O(1) space - where n is the length of the input array
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.binarySearch(nums, target, True), self.binarySearch(nums, target, False)]
    
    def binarySearch(self, nums, target, leftBias):
        l, r = 0, len(nums) - 1
        i = -1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                i = m
                if leftBias:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return i
    
