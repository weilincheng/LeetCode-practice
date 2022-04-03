class Solution:
    # O(log(n)) time | O(1) space - where n is the input integer
    def isPerfectSquare(self, num: int) -> bool:        
        l, r = 1, num
        while l <= r:
            m = l + (r - l) // 2
            if num == m ** 2:
                return True
            elif num < m ** 2:
                r = m - 1
            else:
                l = m + 1
        return False
        