class Solution:
    # O(nlog(n)) time | O(n) space - where is the length of the inpu array
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m = len(mat)
        rows = sorted(range(m), key=lambda i: (mat[i], i))
        return rows[:k]
