class Solution:
    # O(m + n) time | O(1) space - where m is the row and n is the col of the matrix
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = 0, len(matrix[0]) - 1
        while r < len(matrix) and c >= 0:
            if target == matrix[r][c]:
                return True
            if target > matrix[r][c]:
                r += 1
            else:
                c -= 1
        return False
    