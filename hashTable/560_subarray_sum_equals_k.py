class Solution:
    # O(n) time | O(n) space - where n is the length of the input array
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {0:1}
        currSum = 0
        result = 0
        for num in nums:
            currSum += num
            diff = currSum - k
            result += prefixSum.get(diff, 0)
            prefixSum[currSum] = prefixSum.get(currSum, 0) + 1
        return result
    