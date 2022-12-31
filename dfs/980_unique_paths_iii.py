class Solution:
    # O(4^m*n) time | O(m*n) space
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        squares = 1
        startR, startC = 0, 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    squares += 1
                elif grid[r][c] == 1:
                    startR, startC = r, c
        
        def backtrack(r, c, squares):
            if r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] == -1:
                return 0
            if grid[r][c] == 2:
                return squares == 0
            uniquePaths = 0
            grid[r][c] = -1
            directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
            for dr, dc in directions:
                uniquePaths += backtrack(r + dr, c + dc, squares - 1)
            grid[r][c] = 0
            return uniquePaths

        return backtrack(startR, startC, squares)

