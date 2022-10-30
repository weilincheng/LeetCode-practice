class Solution:
    # O(m*n*k) time | O(m*n*k) space
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        ROW, COL = len(grid), len(grid[0])
        if k >= ROW + COL - 2: return ROW + COL - 2
        q = deque([(0, 0, 0, 0)]) # (r, c, obstacles, minSteps)
        visit = {}
        while q:
            r, c, obstacles, minSteps = q.popleft()
            if r < 0 or r == ROW or c < 0 or c == COL: continue
            if r == ROW - 1 and c == COL - 1:
                return minSteps
            obstacles += grid[r][c]
            if obstacles >= visit.get((r, c), float('inf')) or obstacles > k: continue
            visit[(r, c)] = obstacles
            dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in dirs:
                q.append((r + dr, c + dc, obstacles, minSteps + 1))
            
        return -1
    
