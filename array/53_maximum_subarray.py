class Solution
    # O(n) time | O(1) space - where n is the length of the input list
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = currentSum = nums[0]
        
        for i in range(1, len(nums)):
            currentSum = max(currentSum + nums[i], nums[i])
            maxSum = max(currentSum, maxSum)
            
        return maxSum