class Solution:
    # O(n) time | O(n) space - where n is tokens.length
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            "+" : lambda a, b: a + b,
            "-" : lambda a, b: a - b,
            "*" : lambda a, b: a * b,
            "/" : lambda a, b: int(a / b)
        }
        for token in tokens:
            if token in ops:
                b, a = stack.pop(), stack.pop()
                stack.append(ops[token](a, b))
            else:
                stack.append(int(token))
        return stack[0]

