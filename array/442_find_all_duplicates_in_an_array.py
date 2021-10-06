class Solution:
    # Loop each number and use it as index. Times the value at correponding index by -1.
    # Whenever encounter a value which is less than zero, it is a duplicate number
    # O(n) time | O(1) space - where n is the length of the input array
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                res.append(abs(num))
            nums[idx] = -nums[idx]
        return res
    