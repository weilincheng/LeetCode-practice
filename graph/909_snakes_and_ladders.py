class Solution:
    # O(n^2) time | O(n^2) space 
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def squareToPos(square):
            r = n - 1 - ((square - 1) // n)
            c = (square - 1) % n
            if n % 2 == r % 2:
                c = n - 1 - c
            return [r, c]

        q = deque() # [square, moves]
        q.append([1, 0])
        visit = set()
        while q:
            square, moves = q.popleft()
            for i in range(1, 7):
                nextSquare = square + i
                r, c = squareToPos(nextSquare)
                if board[r][c] != -1:
                    nextSquare = board[r][c]
                if nextSquare == n ** 2:
                    return moves + 1
                if nextSquare not in visit:
                    q.append([nextSquare, moves + 1])
                    visit.add(nextSquare)
        return -1

