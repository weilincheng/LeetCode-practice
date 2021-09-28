class Solution:
    # Use two pointers
    # O(n) time | O(n) space - where n is the length of the input array 
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:        
        ans = [None for _ in range(len(nums))]
        oddIdx = 1
        evenIdx = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                ans[evenIdx] = nums[i]
                evenIdx += 2
            else:
                ans[oddIdx] = nums[i]
                oddIdx += 2
        return ans
                