class MyStack:

    def __init__(self):
        self.q = deque()
        
    # O(n) time | O(1) space 
    def push(self, x: int) -> None:
        self.q.append(x)
        curSize = len(self.q)
        for _ in range(curSize - 1):
            self.q.append(self.q.popleft())

    # O(1) time 
    def pop(self) -> int:
        return self.q.popleft()
        

    def top(self) -> int:
        return self.q[0]
        

    def empty(self) -> bool:
        return len(self.q) == 0
        