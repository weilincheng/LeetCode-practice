class Solution:
    # O(log(n)) time in average | O(1) space - where n is the input integer
    def minSteps(self, n: int) -> int:
        if n == 1: return 0
        steps, curLen, copyLen = 0, 1, 1
        while cur < n:
            nextCopyLen = curLen + copyLen
            curLen += copyLen
            if (n - nextCopyLen) % nextCopyLen:
                steps += 1
            else:
                copyLen = nextCopyLen
                steps += 2
        return steps
