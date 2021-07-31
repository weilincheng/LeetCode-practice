# Time: O(1) | Space: O(1)
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        if len(self.minStack) == 0 or val <= self.minStack[len(self.minStack) - 1]:
            self.minStack.append(val)
        
        self.stack.append(val)
        

    def pop(self) -> None:
        if self.stack[len(self.stack) - 1] == self.minStack[len(self.minStack) - 1]:
            self.minStack.pop()
        
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]
        

    def getMin(self) -> int:
        return self.minStack[len(self.minStack) - 1]
