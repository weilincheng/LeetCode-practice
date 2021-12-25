class Solution:
    # O(n) time | O(n) space - where n is the length of the input string
    def calculate(self, s: str) -> int:
        stack = []
        currentNumber = 0
        operation = "+"
        for i, char in enumerate(s):
            if char.isdigit():
                currentNumber = currentNumber * 10 + int(char)
            if not char.isdigit() and char != " " or i == len(s) - 1:
                if operation == '-':
                    stack.append(-currentNumber)
                elif operation == '+':
                    stack.append(currentNumber)
                elif operation == '*':
                    stack.append(stack.pop() * currentNumber)
                elif operation == '/':
                    stack.append(int(stack.pop() / currentNumber))
                operation = char
                currentNumber = 0
        res = 0
        while stack:
            res += stack.pop()
            
        return res
    