class FreqStack:
    # O(1) time | O(n) space - where n is the number of element in FreqStack
    def __init__(self):
        self.count = {}
        self.stacks = {}
        self.maxCount = 0
    
    def push(self, val: int) -> None:
        self.count[val] = self.count.get(val, 0) + 1
        if self.count[val] > self.maxCount:
            self.maxCount = self.count[val]
            self.stacks[self.count[val]] = []
        self.stacks[self.count[val]].append(val)

    def pop(self) -> int:
        if self.stacks[self.maxCount]:
            valToPop = self.stacks[self.maxCount].pop()
            self.count[valToPop] -= 1
            if not self.stacks[self.maxCount]:
                self.maxCount -= 1
            return valToPop
            