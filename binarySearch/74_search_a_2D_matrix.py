class Solution:
    # O(log(m) + log(n)) time | O(1) space 
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        
        topRow, bottomRow = 0, rows - 1
        while topRow <= bottomRow:
            midRow = topRow + (bottomRow - topRow) // 2
            if matrix[midRow][0] <= target <= matrix[midRow][cols - 1]:
                left, right = 0, cols - 1
                while left <= right:
                    mid = left + (right - left) // 2
                    if target == matrix[midRow][mid]:
                        return True
                    elif target < matrix[midRow][mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
                return False
            elif target < matrix[midRow][0]:
                bottomRow = midRow - 1
            else:
                topRow = midRow + 1
        return False

class Solution2:
    # O(log(m*n)) time | O(1) space
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1
        while left <= right:
            mid = left + (right - left) // 2
            r, c = mid // cols, mid % cols
            midVal = matrix[r][c]
            if midVal < target:
                left = mid + 1
            elif midVal > target:
                right = mid - 1
            else:
                return True
        return False
