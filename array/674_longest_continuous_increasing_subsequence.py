class Solution:
    # O(n) time | O(1) space - where n is the length of the input array
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        max_count = count = 1
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                count += 1
            else:
                count = 1
            max_count = max(max_count, count)
        return max_count
