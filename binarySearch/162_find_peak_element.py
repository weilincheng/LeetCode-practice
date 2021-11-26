class Solution:
    # O(log(n)) time | O(1) space - where n is the length of nums
    def findPeakElement(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid
            elif nums[mid] > nums[mid + 1] and nums[mid] < nums[mid - 1]:
                hi = mid - 1 # mid - 1 might be the possible peak
            else:
                lo = mid + 1 # mid + 1 might be the possible peak
        return lo
    