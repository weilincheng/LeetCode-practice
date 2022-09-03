class Solution:
    # O(2^n) time | O(n) space - where n is the number of digits
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = []
        if n == 1:
            res.append(0)
            
        def dfs(n, num):
            if n == 0:
                return res.append(num)
            tailDigit = num % 10
            if tailDigit + k < 10:
                dfs(n - 1, num * 10 + tailDigit + k)
            if tailDigit - k >= 0 and k != 0:
                dfs(n - 1, num * 10 + tailDigit - k)
                    
        for num in range(1, 10):
            dfs(n - 1, num)
        
        return res

