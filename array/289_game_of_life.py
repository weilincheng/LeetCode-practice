class Solution:
    # O(n) time | O(1) space - where n is the number of cells
    def gameOfLife(self, board: List[List[int]]) -> None:
        rows, cols = len(board), len(board[0])

        def countLiveNeighbors(r, c):
            nei = 0
            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    if (i == r and j == c) or i < 0 or i == rows or j < 0 or j == cols: 
                        continue
                    if board[i][j] in [1, 3]:
                        nei += 1
            return nei
        
        for r in range(rows):
            for c in range(cols):
                nei = countLiveNeighbors(r, c)
                if board[r][c] == 1 and 2 <= nei <= 3:
                    board[r][c] = 3
                elif nei == 3:
                    board[r][c] = 2

        for r in range(rows):
            for c in range(cols):
                board[r][c] //= 2
                