class Solution:
    # O(n) time | O(n) space - where n is s.length
    def minFlipsMonoIncr(self, s: str) -> int:
        dp = {}
        def dfs(i, mono):
            if i == len(s): return 0
            if (i, mono) in dp:
                return dp[(i, mono)]
            
            if mono and s[i] == "0":
                dp[(i, mono)] = min(1 + dfs(i + 1, False), dfs(i + 1, mono))
            elif mono and s[i] == "1":
                dp[(i, mono)] = min(1 + dfs(i + 1, mono), dfs(i + 1, False))
            elif not mono and s[i] == "0":
                dp[(i, mono)] = 1 + dfs(i + 1, mono) 
            else:
                dp[(i, mono)] = dfs(i + 1, mono)            
            return dp[(i, mono)]
        
        return dfs(0, True)
