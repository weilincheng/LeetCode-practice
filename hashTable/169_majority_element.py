class Solution:
    # O(n) time | O(n) space 
    def majorityElement(self, nums: List[int]) -> int:
        majoritySize = len(nums) / 2
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            if count[num] >= majoritySize:
                return num
        