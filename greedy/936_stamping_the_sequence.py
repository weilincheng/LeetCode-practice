class Solution:
    # O(N * (N - M) * M) time | O(N + M) space 
    # where N is len(target), and M is len(stamp)
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        M, N = len(stamp), len(target)
        s, t = list(stamp), list(target)
        res = []
        
        def check(i):
            changed = False
            for j in range(M):
                if t[i + j] == "?": continue
                if t[i + j] != s[j]: return False
                changed = True
            if changed:
                for j in range(M):
                    t[i + j] = "?"
                res.append(i)
            return changed
        
        changed = True
        while changed:
            changed = False
            for i in range(N - M + 1):
                changed |= check(i)
                
        return res[::-1] if t == ["?"] * N else []

