class Solution:
    # O(n) time | O(1) space - where n is the length of the input list
    def minCostToMoveChips(self, position: List[int]) -> int:
        even_count = odd_count = 0
        for num in position:
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        return min(even_count, odd_count)
    