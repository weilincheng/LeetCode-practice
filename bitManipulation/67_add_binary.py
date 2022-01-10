class Solution:
    # O(n) time | O(1) space - where n is the length of the input strings
    def addBinary(self, a: str, b: str) -> str:
        carry = 0 
        res = ""
        a, b = a[::-1], b[::-1]
        
        for i in range(max(len(a), len(b))):
            digitA = ord(a[i]) - ord("0") if i < len(a) else 0
            digitB = ord(b[i]) - ord("0") if i < len(b) else 0
            
            total = digitA + digitB + carry
            char = str(total % 2)
            res = char + res
            carry = total // 2
            
        if carry:
            res = "1" + res
        
        return res
