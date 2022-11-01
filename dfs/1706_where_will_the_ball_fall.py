class Solution:
    # O(m*n) time | O(m) space 
    # where m is the number of rows and n is the number of cols
    def findBall(self, grid: List[List[int]]) -> List[int]:
        ROWS, COLS = len(grid), len(grid[0])
        res = [] * COLS 

        def dfs(r, c):
            if r == ROWS:
                return c
            nextC = c + grid[r][c]
            if nextC < 0 or nextC == COLS or grid[r][c] != grid[r][nextC]:
                return -1
            
            return dfs(r + 1, nextC)
        
        for c in range(COLS):
            res[c] = dfs(0, c)
        
        return res

