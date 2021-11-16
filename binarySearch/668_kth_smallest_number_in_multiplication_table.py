class Solution:
    # O(m * log(m * n)) time | O(1) space
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def enough(x):
            count = 0
            for i in range(1, m + 1):
                count += min(x // i, n)
                if count >= k: return True
            return False
        
        left, right = 1, m * n
        while left < right:
            middle = left + (right - left) // 2
            if enough(middle):
                right = middle 
            else:
                left = middle + 1
        return left 
    