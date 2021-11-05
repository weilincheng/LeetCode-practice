class Solution:
    # O(log(n)) time | O(1) space 
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            middle = (left + right) // 2
            potentialMatch = middle * (middle + 1) // 2
            if n == potentialMatch:
                return middle
            elif n > potentialMatch:
                left = middle + 1
            else:
                right = middle - 1
        return right 
    