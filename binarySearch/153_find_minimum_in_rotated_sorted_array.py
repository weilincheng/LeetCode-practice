class Solution:
    # O(log(n)) time | O(1) space - where n is the length of the input array
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        res = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            m = (l + r) // 2
            res = min(nums[m], res)
            if nums[m] >= nums[l]: # Edge case that m == l
                l = m + 1
            else:
                r = m - 1
                
        return res

