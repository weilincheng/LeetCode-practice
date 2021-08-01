# Time: O(1) | Space: O(1)
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []


    def push(self, val: int) -> None:
        newMin = val
        if len(self.minStack):
            newMin = min(self.minStack[len(self.minStack) - 1], val)
            
        self.minStack.append(newMin)
        self.stack.append(val)
        

    def pop(self) -> None:
        self.minStack.pop()
        self.stack.pop()
        
        
    def top(self) -> int:
        return self.stack[len(self.stack) - 1]
        

    def getMin(self) -> int:
        return self.minStack[len(self.minStack) - 1]
