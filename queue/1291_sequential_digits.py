class Solution:
    # O(45) time | O(45) space since there are only 9 + 8 ... + 1 numbers with sequential digit
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        queue = deque(range(1, 10))
        while queue:
            elem = queue.popleft()
            if elem >= low and elem <= high:
                result.append(elem)
            if elem % 10 < 9:
                elem = elem * 10 + (elem % 10 + 1)
                queue.append(elem)
        return result 
    