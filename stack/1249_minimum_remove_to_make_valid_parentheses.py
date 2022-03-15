class Solution:
    # O(n) time | O(n) space - where n is the length of the input string
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = []
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack:
                    stack.pop()
                else:
                    s[i] = ""
        
        while stack:
            i = stack.pop()
            s[i] = ""
    
        return "".join(s)
