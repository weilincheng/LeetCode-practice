class Solution:
    # O(m * n) time | O(m * n) space
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def dfsHelper(i, j):
            if i < 0 or i > rows - 1 or j < 0 or j > cols - 1 or board[i][j] != 'O': return
            board[i][j] = '#'
            dfsHelper(i - 1, j)
            dfsHelper(i + 1, j)
            dfsHelper(i, j - 1)
            dfsHelper(i, j + 1)
        
        for i in range(rows):
            dfsHelper(i, 0)
            dfsHelper(i, cols - 1)
        for j in range(cols):
            dfsHelper(0, j)
            dfsHelper(rows - 1, j)
            
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
    