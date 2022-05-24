class Solution:
    # O(n) time | O(n) space - where n is the length of the input string
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        length = maxLength = 0
        for idx, c in enumerate(s):
            if c == "(":
                stack.append(idx)
            else:
                stack.pop()
                if not stack:
                    stack.append(idx)
                else:
                    length = idx - stack[-1]
                    maxLength = max(maxLength, length)
        return maxLength

