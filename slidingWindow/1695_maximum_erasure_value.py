class Solution:
    # O(n) time | O(n) space - where n is the length of the input array
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res, curSum, l = 0, 0, 0
        scoreSet = set()
        for r in range(len(nums)):
            while nums[r] in scoreSet:
                scoreSet.remove(nums[l])
                curSum -= nums[l]     
                l += 1
            curSum += nums[r]
            scoreSet.add(nums[r])
            res = max(res, curSum)
        return res

