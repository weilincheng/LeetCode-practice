class Solution:
    # O(n^2) time | O(n^2) space - wher n^2 is the number of cells 
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1: return -1
        q = deque([(1, 0, 0)])
        visit = set()
        adj = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        while q:
            dist, r, c = q.popleft()
            if r == c == n - 1:
                return dist 
            if 0 <= r < n and 0 <= c < n and grid[r][c] == 0 and (r, c) not in visit:
                for dR, dC in adj:
                    nextR, nextC = r + dR, c + dC
                    q.append((dist + 1, nextR, nextC))
                    visit.add((r, c))
        return -1
