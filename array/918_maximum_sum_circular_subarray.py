class Solution:
    # O(n) time | O(1) space - where n is nums.length
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globMax = globMin = nums[0]
        curMax = curMin = total = 0
        for num in nums:
            curMax = max(curMax + num, num)
            curMin = min(curMin + num, num)
            total += num
            globMax = max(globMax, curMax)
            globMin = min(globMin, curMin)
        
        return max(globMax, sum(nums) - globMin) if globMax > 0 else globMax

