class Solution:
    # O(n) time | O(1) space - where n is the length of the input array
    def minOperations(self, nums: List[int], x: int) -> int:
        targetSum = sum(nums) - x
        if targetSum < 0: return -1
        maxLen = -1
        l = curSum = 0
        for r in range(len(nums)):
            curSum += nums[r]
            while l <= r and curSum > targetSum:
                curSum -= nums[l]
                l += 1
            if curSum == targetSum:
                maxLen = max(maxLen, r - l + 1)
        return -1 if maxLen == -1 else len(nums) - maxLen
    
