class Solution:
    # O(m*n) time | O(m*n) space 
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        ans = [[0 for _ in range(m)] for _ in range(n)]
        
        for r in range(m):
            for c in range(n):
                ans[c][r] = matrix[r][c]
        return ans
    
