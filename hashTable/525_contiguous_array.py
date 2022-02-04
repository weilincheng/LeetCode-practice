class Solution:
    # O(n) time | O(n) space - where n is the length of the input array
    def findMaxLength(self, nums: List[int]) -> int:
        countMap = {0: -1}
        count, maxLen = 0, 0
        for idx, num in enumerate(nums):
            count += 1 if num == 1 else -1
            if count in countMap:
                maxLen = max(maxLen, idx - countMap[count])
            else:
                countMap[count] = idx
        return maxLen
    