class Solution:
    # O(n) time | O(26) space - where n is the length of the string
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        visited = set()
        idxMap = {c: i for i, c in enumerate(s)}
            
        for i, c in enumerate(s):
            if c in visited: continue
            while stack and ord(stack[-1]) > ord(c) and idxMap[stack[-1]] > i:
                visited.remove(stack.pop())

            stack.append(c)
            visited.add(c)
            
        return "".join(stack)
