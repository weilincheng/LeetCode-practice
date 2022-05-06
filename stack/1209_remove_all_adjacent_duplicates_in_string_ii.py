class Solution:
    # O(n) time | O(n) space
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [] # [char, count]
        for char in s:
            if not stack or stack[-1][0] != char:
                stack.append([char, 1])
            else:
                stack[-1][1] += 1
            
            if stack[-1][1] == k:
                stack.pop()

        return "".join(char * count for char, count in stack)
