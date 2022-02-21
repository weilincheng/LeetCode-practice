class Solution:
    # O(n) time | O(n) space 
    def majorityElement(self, nums: List[int]) -> int:
        majoritySize = len(nums) / 2
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            if count[num] >= majoritySize:
                return num

class Solution2:
    # O(n) time | O(1) space - where n is the lenght of the array
    def majorityElement(self, nums: List[int]) -> int:
        count, result = 0, 0
        
        for num in nums:
            if count == 0:
                result = num
            
            count += 1 if result == num else -1
            
        return result
         