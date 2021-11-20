class Solution:
    # O(log(n)) time | O(1) space - where n is the length of the input array
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            middle = low + (high - low) // 2
            pair = middle + 1 if middle % 2 == 0 else middle - 1
            if nums[middle] == nums[pair]:
                low = middle + 1
            else:
                high = middle
        return nums[low]
    