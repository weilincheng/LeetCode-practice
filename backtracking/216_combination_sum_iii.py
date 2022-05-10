class Solution:
    # O(9!/k!/(9-k)!) time | O(k) space 
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(n, curComb, nextNum):
            if len(curComb) == k: 
                if n == 0:
                    res.append(curComb.copy())
                return
            for num in range(nextNum, 10):
                if num > n:
                    return
                curComb.append(num)
                backtrack(n - num, curComb, num + 1)
                curComb.pop()

        res = []
        backtrack(n, [], 1)
        
        return res
    