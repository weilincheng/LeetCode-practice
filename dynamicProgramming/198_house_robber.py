class Solution:
    # O(n) time | O(1) space - where n is the length of the input array
    def rob(self, nums: List[int]) -> int:
        rob1 = rob2 = 0
        # [rob1, rob2, num, num + 1]
        for num in nums:
            temp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
