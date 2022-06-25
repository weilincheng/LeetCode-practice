class Solution:
    # O(n) time | O(1) space - where n is nums.length
    def checkPossibility(self, nums: List[int]) -> bool:
        p, n = -1, len(nums)
        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                if p != -1:
                    return False
                p = i
        
        return p in [-1, 1, n - 1] or nums[p - 2] <= nums[p] or nums[p - 1] <= nums[p + 1]
    
