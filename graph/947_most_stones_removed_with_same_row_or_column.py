class Solution:
    # O(n) time | O(n) space - where n is the number of stones
    def removeStones(self, stones: List[List[int]]) -> int:
        points = {(r, c) for r, c in stones}
        island = 0
        rows, cols = defaultdict(list), defaultdict(list)
        
        def dfs(row, col):
            points.remove((row, col))
            for c in rows[row]:
                if (row, c) in points:
                    dfs(row, c)
            
            for r in cols[col]:
                if (r, col) in points:
                    dfs(r, col)
        
        for r, c in stones:
            rows[r].append(c)
            cols[c].append(r)
        
        for r, c in stones:
            if (r, c) in points:
                dfs(r, c)
                island += 1
        
        return len(stones) - island
    
