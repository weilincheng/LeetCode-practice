class Solution:
    # O(n^2) time | O(n) space - where n is the length of the input array
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        for i in range(len(nums) - 2):
            if i == 0 or nums[i] != nums[i - 1]:
                left, right = i + 1, len(nums) - 1
                while left < right:
                    currentSum = nums[i] + nums[left] + nums[right]
                    if currentSum == 0:
                        triplets.append([nums[i], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]: left += 1
                        while left < right and nums[right] == nums[right - 1]: right -= 1
                        left += 1
                        right -= 1
                    elif currentSum > 0:
                        right -= 1
                    else:
                        left += 1
        return triplets 
    