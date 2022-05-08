class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = [[nestedList, 0]]
    
    def next(self) -> int:
        stack = self.stack
        nestedList, i = stack[-1]
        stack[-1][1] += 1
        return nestedList[i].getInteger()
    
    def hasNext(self) -> bool:
        stack = self.stack
        while stack:
            nestedList, i = stack[-1]
            if i == len(nestedList):
                stack.pop()
            else:
                element = nestedList[i]
                if element.isInteger():
                    return True
                stack[-1][1] += 1
                stack.append([element.getList(), 0])
        return False
         