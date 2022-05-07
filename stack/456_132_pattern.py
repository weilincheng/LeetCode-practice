class Solution:
    # O(n) time | O(n) space - where n is the length of the array
    def find132pattern(self, nums: List[int]) -> bool:
        stack = [] # pair of num, minLeft
        curMin = nums[0]
        for num in nums[1:]:
            while stack and num >= stack[-1][0]:
                stack.pop()
            if stack and stack[-1][1] < num:
                return True
            stack.append((num, curMin))
            curMin = min(curMin, num)  
        return False
