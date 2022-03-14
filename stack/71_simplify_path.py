class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        for i in range(len(path)):
            c = path[i]
            if c == "/" and ((res and res[-1] != "/") or not res):
                res.append(c)
            elif c == "." and path[i + 1] == ".":
                if res: 
                    res.pop()
            elif c == ".":
                continue
            else:
                res.append(c)
        return "".join(res)
    