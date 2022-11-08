class Solution:
    # O(n) time | O(n) space
    def makeGood(self, s: str) -> str:
        res = []
        for c in s:
            if res and self.isBad(c, res[-1]): 
                res.pop()
            else:
                res.append(c)

        return "".join(res)
    
    def isBad(self, c1, c2):
        if c1 > c2:
            c1, c2 = c2, c1
        return ord(c1) - ord("A") == ord(c2) - ord("a")

