class Solution:
    # O(n) time | O(m) space - where n is the lenght of the input list
    # m is the number of unique numbers in the input list
    def removeDuplicates(self, nums: List[int]) -> int:
        count = {}
        slow, fast = 0, 0
        while fast < len(nums):
            currNum = nums[fast]
            count[currNum] = count.get(currNum, 0) + 1
            if count[currNum] < 3:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow 
    