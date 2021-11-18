class Solution:
    # O(n) time | O(1) space - where n is the length of the input array
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return []
        ans = []
        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0: nums[index] *= -1
        for index, num in enumerate(nums):
            if num > 0:
                ans.append(index + 1)
        return ans
    