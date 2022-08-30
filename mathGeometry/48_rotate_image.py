class Solution:
    # O(n^2) time | O(1) space - where n is the length of the input array
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left, right = 0, len(matrix) - 1
        while left < right:
            top, bottom = left, right
            for i in range(right - left):
                
                # Store the value of left col
                tmp = matrix[top + i][left]
                
                # Move bottom row to left col
                matrix[top + i][left] = matrix[bottom][left + i]
                
                # Move right col to bottom row
                matrix[bottom][left + i] = matrix[bottom - i][right]
                
                # Move top row to right col
                matrix[bottom - i][right] = matrix[top][right - i]
                
                # Set tmp value to top row
                matrix[top][right - i] = tmp
            
            left, right = left + 1, right - 1
        
