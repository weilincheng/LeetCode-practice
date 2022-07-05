class Solution:
    # O(n) time | O(n) space - where n is nums.length
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        res = 0
        for num in nums:
            if num - 1 not in hashSet:
                curLen = 1
                while num + 1 in hashSet:
                    curLen += 1
                    num += 1
                res = max(res, curLen)
        return res
    
