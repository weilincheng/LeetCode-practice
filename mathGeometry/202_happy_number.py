class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOfSquare(n):
            curSum = 0
            while n:
                curSum += (n % 10) ** 2
                n //= 10
            return curSum

        slow = n
        fast = sumOfSquare(n)
        while fast != 1 and slow != fast:
            slow = sumOfSquare(slow)
            fast = sumOfSquare(sumOfSquare(fast))
        
        return fast == 1

