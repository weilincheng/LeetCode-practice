class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.peekVal = self.iterator.next()
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.peekVal
        
        

    def next(self):
        """
        :rtype: int
        """
        
        res = self.peekVal
        self.peekVal = self.iterator.next() if self.iterator.hasNext() else None
        print(self.peekVal)
        return res
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.peekVal is not None
