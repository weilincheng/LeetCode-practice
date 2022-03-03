class Solution:
    # O(n) time | O(1) space - where n is the length of the array
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0, 0]
        ans = 0
        
        for i in range(2, n):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                dp[1] = dp[0] + 1        
            ans += dp[1]
            dp[0], dp[1] = dp[1], 0
            
        return ans
    