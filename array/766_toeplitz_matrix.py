class Solution:
    # O(m*n) time | O(1) space
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        ROW, COL = len(matrix), len(matrix[0])
        
        for r in range(ROW):
            for c in range(COL):
                if r > 0 and c > 0 and matrix[r - 1][c - 1] != matrix[r][c]:
                    return False
        return True

