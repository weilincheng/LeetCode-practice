class Solution:
    # O(n^2) time | O(n) space 
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = diff = float('inf')
        nums.sort()
        
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                curSum = nums[l] + nums[r] + nums[i]
                curDiff = abs(target - curSum)
                if curDiff < diff: 
                    res, diff = curSum, curDiff
                if curSum == target:
                    return curSum
                elif curSum > target:
                    r -= 1
                else:
                    l += 1
                    
        return res

