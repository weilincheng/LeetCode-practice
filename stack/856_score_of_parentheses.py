class Solution:
    # O(n) time | O(n) space - where n is the length of the string
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for c in s:
            if c == "(":
                stack.append(0)
            else:
                score = stack.pop() 
                stack[-1] += max(2 * score, 1)
        
        return stack.pop()
    