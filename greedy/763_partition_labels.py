class Solution:
    # O(n) time | O(26) space - where n is the length of the string
    def partitionLabels(self, s: str) -> List[int]:
        lastIdx = {c: i for i, c in enumerate(s)}
        left, right = 0, 0
        res = []
        for i, c in enumerate(s):
            right = max(right, lastIdx[c])
            if i == right:
                res.append(i - left + 1)
                left = i + 1
        return res
