class Solution:
    # O(n) time | O(1) space 
    def myAtoi(self, s: str) -> int:
        index = 0
        ans = 0
        sign = 1
        n = len(s)
        if not n: return 0
        
        INT_MAX = pow(2, 31) - 1
        INT_MIN = -pow(2, 31)
        
        while index < n and s[index] == " ":
            index += 1
        
        if index < n and s[index] == "+":
            sign = 1
            index += 1
        elif index < n and s[index] == "-":
            sign = -1
            index += 1
        
        while index < n and s[index].isdigit():
            digit = int(s[index])
            
            if ans > INT_MAX // 10 or (ans == INT_MAX // 10 and digit > INT_MAX % 10):
                return INT_MAX if sign == 1 else INT_MIN
            
            ans = 10 * ans + digit
            index += 1
        
        return sign * ans
        