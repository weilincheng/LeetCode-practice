class Solution:
    # O(n^2) time | O(32n) space - where n is the length of the input array
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        
        nums.sort()
        sol = [[num] for num in nums]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(sol[i]) <= len(sol[j]):
                    sol[i] = sol[j] + [nums[i]]
        return max(sol, key=len)
    