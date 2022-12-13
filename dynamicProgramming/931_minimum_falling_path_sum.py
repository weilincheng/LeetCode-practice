class Solution:
    # O(n) time | O(1) space - where n is the number of cells 
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        for r in range(1, ROWS):
            for c in range(COLS):
                upperLeft = matrix[r - 1][max(0, c - 1)]
                upperMid = matrix[r - 1][c]
                upperRight = matrix[r - 1][min(COLS - 1, c + 1)]
                matrix[r][c] += min(upperLeft, upperMid, upperRight)
        return min(matrix[ROWS - 1])
    
