class Solution:
    # O(n) time | O(n) space - where n is the length of the input list
    def containsDuplicate(self, nums: List[int]) -> bool:
        numCount = {}
        for num in nums:
            if num in numCount:
                numCount[num] += 1
                if numCount[num] == 2:
                    return True
            else:
                numCount[num] = 1
        return False
