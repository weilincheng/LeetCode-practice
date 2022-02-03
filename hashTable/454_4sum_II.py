class Solution:
    # O(n^2) time | O(n) space 
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        seenNum = {}
        for num1, num2 in product(nums1, nums2):
            currSum = num1 + num2
            seenNum[currSum] = seenNum.get(currSum, 0) + 1
        
        result = 0
        for num3, num4 in product(nums3, nums4):
            currSum = num3 + num4
            result += seenNum.get(-currSum, 0)
        
        return result 
    