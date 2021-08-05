# O(n) time | O(1) space
class Solution:
    def fib(self, n: int) -> int:
        lastTwo = [0, 1]
        counter = 2
        while counter <= n:
            nextFib = lastTwo[0] + lastTwo[1]
            lastTwo[0] = lastTwo[1]
            lastTwo[1] = nextFib
            counter += 1
            
        return lastTwo[1] if n > 0 else lastTwo[0]
