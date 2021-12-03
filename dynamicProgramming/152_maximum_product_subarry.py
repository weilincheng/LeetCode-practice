class Solution:
    # O(n) time | O(1) space - where n is the length of the input array
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currentMax, currentMin = 1, 1
        for num in nums:
            if num == 0:
                currentMax, currentMin = 1, 1
                continue
            tmp = currentMax * num
            currentMax = max(currentMax * num, currentMin * num, num)
            currentMin = min(tmp, currentMin * num, num)
            res = max(currentMax, res)
        return res
    