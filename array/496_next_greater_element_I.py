class Solution:
    # O(n) time | O(n) space - where n is the length of the input array
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nextGreatest = {}
        for num in nums2:
            while stack and stack[-1] < num:
                nextGreatest[stack.pop()] = num
            stack.append(num)
            
        for i in range(len(nums1)):
            nums1[i] = nextGreatest.get(nums1[i], -1)
        return nums1
    