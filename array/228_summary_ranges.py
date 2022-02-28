class Solution:
    # O(n) time | O(1) space - where n is the length of the string
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return nums
        res, curr, start = [], 0, 0
        while curr < len(nums) - 1:
            if nums[curr] + 1 != nums[curr + 1]:
                res.append(self.print_range(start, curr, nums))
                start = curr + 1
            curr += 1
        
        res.append(self.print_range(start, curr, nums))
        
        return res
        
    def print_range(self, start, curr, nums):
        return f'{nums[start]}' if start == curr else f'{nums[start]}->{nums[curr]}'
    