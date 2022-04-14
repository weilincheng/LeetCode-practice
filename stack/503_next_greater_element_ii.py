class Solution:
    # O(n) time | O(n) space - where n is the length of the input array
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack, ans = [], [-1] * len(nums)
        
        for i in range(len(nums) * 2):
            i %= len(nums)
            while stack and nums[stack[-1]] < nums[i]:
                ans[stack.pop()] = nums[i]
            stack.append(i)
            
        return ans
    