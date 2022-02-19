class Solution:
    # O(n) time | O(n) space - where n is the length of the string
    def removeKdigits(self, num: str, k: int) -> str:
        strLen = len(num)
        if k == strLen: return "0"
        stack = []
        
        for n in num:
            while stack and k and stack[-1] > n:
                stack.pop()
                k -= 1
            if stack or n != "0":
                stack.append(n)
        
        if k > 0:
            stack = stack[:-k]
            
        return "".join(stack) or "0"
    