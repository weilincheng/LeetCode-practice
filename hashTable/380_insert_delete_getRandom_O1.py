class RandomizedSet:
    # O(1) time - Use dict for insert and remove; use an array to return an random number
    def __init__(self):
        self.numbers, self.position = [], {}

    def insert(self, val: int) -> bool:
        if val in self.position:
            return False
        self.numbers.append(val)
        self.position[val] = len(self.numbers) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.position:
            return False
        idxOfElementToRemove, lastElement = self.position[val], self.numbers[-1]
        self.position[lastElement] = idxOfElementToRemove
        self.numbers[idxOfElementToRemove] = lastElement
        self.numbers.pop()
        self.position.pop(val)
        return True

        
    def getRandom(self) -> int:
        idx = randrange(0, len(self.numbers))
        return self.numbers[idx]
