class Solution:
    # O(n) time | O(1) space
    def minStartValue(self, nums: List[int]) -> int:
        minSum, currentSum = nums[0], 0
        for num in nums:
            currentSum += num
            minSum = min(minSum, currentSum)
        if minSum < 0:
            return abs(minSum) + 1
        else:
            return 1
        