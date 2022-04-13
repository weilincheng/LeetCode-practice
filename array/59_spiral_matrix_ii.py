class Solution:
    # O(n^2) time | O(n^2) space - where n is the input integer
    def generateMatrix(self, n: int) -> List[List[int]]:
        left, right = 0, n
        top, bottom = 0, n
        res = [[0 for _ in range(n)] for _ in range(n)]
        order = 1
        while left < right and top < bottom:
            for i in range(left, right):
                res[top][i] = order
                order += 1
            top += 1
            
            for i in range(top, bottom):
                res[i][right - 1] = order
                order += 1
            right -= 1
            
            if not (left < right and top < bottom):
                break
            
            for i in reversed(range(left, right)):
                res[bottom - 1][i] = order
                order += 1
            bottom -= 1
            
            for i in reversed(range(top, bottom)):
                res[i][left] = order
                order += 1
            left += 1
            
        return res
