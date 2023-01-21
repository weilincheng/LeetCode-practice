class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        if len(s) > 12 or len(s) < 4:
            return res
        
        def backtrack(i, curIP):
            if i == len(s) and len(curIP) == 4:
                res.append(".".join(curIP))
                return
            if len(curIP) > 4:
                return
            
            for j in range(i, min(i + 3, len(s))):
                if int(s[i:j+1]) < 256 and (i == j or s[i] != "0"):
                    curIP.append(s[i:j+1])
                    backtrack(j + 1, curIP)
                    curIP.pop()
        
        backtrack(0, [])
        return res

