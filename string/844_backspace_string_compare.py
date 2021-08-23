class Solution:
    # Use stack to store the string after backspacing
    # Comapre the element in two stacks 
    # O(n) time | O(n) space - where n is the length of the input string
    def convertToStack(self, string):
        stack = []
        for char in string:
            if char == "#" and len(stack) > 0:
                stack.pop()
            elif char != "#":
                stack.append(char)
        return stack
    
    def backspaceCompare(self, s: str, t: str) -> bool:
        stackS = self.convertToStack(s)
        stackT = self.convertToStack(t)

        if len(stackS) != len(stackT):
            return False
        
        for i in range(len(stackS)):
            if stackS[i] != stackT[i]:
                return False
        return True
