class Solution:
    # O(n) time | O(1) space - where n is the length of the input array
    def increasingTriplet(self, nums: List[int]) -> bool:
        num1 = num2 = float("inf")
        
        for num in nums:
            if num > num2:
                return True
            if num > num1:
                num2 = min(num2, num)
            num1 = min(num1, num)
        return False

