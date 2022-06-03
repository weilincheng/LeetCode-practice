class NumMatrix:
    # O(m * n) time | O(m * n) space 
    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.prefixSum = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for r in range(m):
            curSum = 0
            for c in range(n):
                curSum += matrix[r][c]
                self.prefixSum[r + 1][c + 1] = curSum + self.prefixSum[r][c + 1]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        bottomRightRegion = self.prefixSum[row2][col2]
        aboveRegion = self.prefixSum[row1 - 1][col2]
        leftRegion = self.prefixSum[row2][col1 - 1]
        topLeftRegion = self.prefixSum[row1 - 1][col1 - 1]
        return bottomRightRegion - aboveRegion - leftRegion + topLeftRegion

