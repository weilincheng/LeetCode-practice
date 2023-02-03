class Solution:
    # O(n) time | O(n) space - where n is s.length
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = []
        increment = numRows * 2 - 2
        for i in range(numRows):
            middleNext = (numRows - 1 - i) * 2
            for j in range(i, len(s), increment):
                res.append(s[j])
                if i > 0 and i < numRows - 1 and j + middleNext <= len(s) - 1:
                    res.append(s[j + middleNext])
        return "".join(res)

