class Solution:
    # O(n*m) time | O(1) space - where n is strs.length and m is strs[i].length 
    def minDeletionSize(self, strs: List[str]) -> int:
        ROWS, COLS = len(strs), len(strs[0])
        if ROWS == 1: return 0
        
        res = 0
        for col in range(COLS):
            for row in range(ROWS - 1):
                if strs[row][col] > strs[row + 1][col]:
                    res += 1
                    break
        return res

