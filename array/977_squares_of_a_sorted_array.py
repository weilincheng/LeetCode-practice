# Time: O(n) | Space: O(n)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squaredArray = [0] * len(nums)
        leftIndex = 0
        rightIndex = len(nums) - 1
        for idx in reversed(range(len(nums))):
            smallerValue = nums[leftIndex]
            largerValue = nums[rightIndex]
            if abs(smallerValue) > abs(largerValue):
                squaredArray[idx] = smallerValue * smallerValue
                leftIndex += 1
            else:
                squaredArray[idx] = largerValue * largerValue
                rightIndex -= 1
        return squaredArray