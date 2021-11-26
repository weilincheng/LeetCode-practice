class Solution:
    # O(log(n)) time | O(1) space - where n is the length of nums
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                low = mid + 1 # The minimum possible index 
            else:
                high = mid # mid can be potential candidate 
        return low
