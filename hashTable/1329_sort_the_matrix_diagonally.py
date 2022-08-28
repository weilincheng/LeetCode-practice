class Solution:
    # O(mnlog(min(m, n))) time | O(mn) space - where m, n the is number of rows and cols
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(mat), len(mat[0])
        diags = defaultdict(list)
        for r in range(ROWS):
            for c in range(COLS):
                diags[r - c].append(mat[r][c])

        for key, value in diags.items():
            diags[key] = sorted(value, reverse=True)

        for r in range(ROWS):
            for c in range(COLS):
                mat[r][c] = diags[r - c].pop()

        return mat
