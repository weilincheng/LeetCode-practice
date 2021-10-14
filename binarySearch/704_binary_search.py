class Solution:
    # Iterative solution 
    # O(log(n)) time | O(1) space - where n is the length of the input array
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            potentialMatch = nums[middle]
            if potentialMatch == target:
                return middle
            elif potentialMatch > target:
                right = middle - 1
            else:
                left = middle + 1
        return -1 
        