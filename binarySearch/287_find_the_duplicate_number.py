class Solution:
    # O(nlog(n)) time | O(1) space - where n is the length of the input array
    def findDuplicate(self, nums: List[int]) -> int:
        low, high = 1, len(nums) - 1
        
        while low <= high:
            middle = low + (high - low) // 2
            count = 0
            
            count = sum(num <= middle for num in nums)
            if count > middle:
                duplicate = middle
                high = middle - 1
            else:
                low = middle + 1
        return duplicate
    