class Solution:
    # O(log(n)) time | O(1) space
    def isUgly(self, n: int) -> bool:
        if n <= 0: return False
        
        primeFactors = [2, 3, 5]
        for factor in primeFactors:
            while n % factor == 0:
                n /= factor
            
        return n == 1

