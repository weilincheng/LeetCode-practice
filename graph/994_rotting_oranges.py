# O(m * n) time | O(m * n) space
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        if rows == 0:
            return -1
        cols, freshCount, rotten = len(grid[0]), 0, deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    freshCount += 1
                elif grid[r][c] == 2:
                    rotten.append((r, c))
        
        minutesElapsed = 0
        while freshCount > 0 and rotten:
            minutesElapsed += 1
            size = len(rotten)
            while size > 0:
                size -= 1
                x, y = rotten.popleft()
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    currentX, currentY = x + dx, y + dy
                    if currentX < 0 or currentX == rows or currentY < 0 or currentY == cols:
                        continue
                    if grid[currentX][currentY] == 2:
                        continue
                    if grid[currentX][currentY] == 1:
                        grid[currentX][currentY] = 2
                        rotten.append((currentX, currentY))
                        freshCount -= 1
        return minutesElapsed if freshCount == 0 else -1
    