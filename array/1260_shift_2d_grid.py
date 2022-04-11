class Solution:
    # O(n) time | O(n) space - where n is the number of grids 
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        k = k % (rows * cols)
        if k == 0:
            return grid
        ans = [[0 for _ in range(cols)] for _ in range(rows)]
        
        for i in range(rows * cols):
            shiftedIdx = i - k
            if shiftedIdx < 0: 
                shiftedIdx += rows * cols
            elif shiftedIdx > rows * cols:
                shiftedIdx %= rows * cols
            ans[i // cols][i % cols] = grid[shiftedIdx // cols][shiftedIdx % cols]
        
        return ans
