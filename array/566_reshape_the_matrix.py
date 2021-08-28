class Solution:
    # O(n) time | O(n) space - where n is the number of element in the input matrix
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row = len(mat)
        column = len(mat[0])
        if row * column != r * c:
            return mat
        newMat = [[0] * c for i in range(r)]       
        newRowNum = 0
        newColumnNum = 0
        for i in range(row):
            for j in range(column):
                newMat[newRowNum][newColumnNum] = mat[i][j]
                newColumnNum += 1
                if newColumnNum == c:
                    newColumnNum = 0
                    newRowNum += 1
        return newMat
