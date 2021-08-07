# O(n) time | O(n) space - where the n is the length of the input string
    def isValid(self, s: str) -> bool:
        opened = ['[', '(', '{']
        closed = [']', ')', '}']
        stack = []
        for character in s:
            if character in opened:
                stack.append(character)
            else:
                if len(stack) == 0 or stack[len(stack) - 1] != opened[closed.index(character)]:
                    return False
                else:
                    stack.pop()
        
        return len(stack) == 0