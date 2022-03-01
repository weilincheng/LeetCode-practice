class Solution:
    # O(n) time | O(1) space - where n is the input integer
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            count = 0
            while i > 0:
                if i < len(res):
                    count += res[i]
                    break
                if i % 2 == 1:
                    count += 1
                i = i // 2
            res.append(count)
        
        return res

class Solution2:
    # O(n) time | O(1) space - where n is the input integer
    def countBits(self, n: int) -> List[int]:
        dp = [0 for _ in range(n + 1)]
        offset = 1
        
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        
        return dp
     