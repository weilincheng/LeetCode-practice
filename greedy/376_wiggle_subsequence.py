class Solution:
    # O(n) time | O(1) space - where n is the nums.length
    def wiggleMaxLength(self, nums: List[int]) -> int:
        N = len(nums)
        if N < 2:
            return N
        prevDiff = nums[1] - nums[0]
        count = 2 if prevDiff != 0 else 1
        for i in range(2, N):
            diff = nums[i] - nums[i - 1]
            if (diff > 0 and prevDiff <= 0) or (diff < 0 and prevDiff >= 0):
                count += 1
                prevDiff = diff
        return count 

