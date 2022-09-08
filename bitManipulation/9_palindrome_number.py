class Solution:
    # O(n) time | O(1) space - where n is the number of digits of x
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        
        dividor = 1
        while x >= 10 * dividor:
            dividor *= 10
            
        while x > 0:
            firstDigit = x // dividor 
            lastDigit = x % 10
            
            if firstDigit != lastDigit: return False
            x = (x % dividor) // 10
            dividor //= 100
        
        return True
    
