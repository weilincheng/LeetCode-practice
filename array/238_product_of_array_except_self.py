class Solution:
    # O(n) time | O(1) space - where n is the length of the input array
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in reversed(range(len(nums))):
            ans[i] *= postfix 
            postfix *= nums[i]
        return ans

