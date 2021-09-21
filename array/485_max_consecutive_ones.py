class Solution:
    # O(n) time | O(1) space - where n is the length of the input array
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = currentMax = 0 
        for num in nums:
            if num == 1:
                currentMax += 1
            else:
                maxCount = max(maxCount, currentMax)
                currentMax = 0
        return max(maxCount, currentMax)
