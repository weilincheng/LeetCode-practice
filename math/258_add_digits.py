class Solution:
    # O(log(n)) time | O(1) space 
    def addDigits(self, num: int) -> int:
        digital_root = 0
        while num > 0:
            digital_root += num % 10
            num = num // 10
            
            if num == 0 and digital_root > 9:
                num = digital_root
                digital_root = 0
            
        return digital_root

class Solution2:
    # O(1) time | O(1) space 
    def addDigits(self, num: int) -> int:
        if num == 0: return 0
        if num % 9 == 0: 
            return 9
        else:
            return num % 9
         