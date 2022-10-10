class Solution:
    # O(n) time | O(n) space - where n is the length of the input string
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1: return ""
        
        res = list(palindrome)
        for i in range(len(res) // 2):
            if res[i] != "a":
                res[i] = "a"
                return "".join(res)
        
        res[-1] = "b"
        return "".join(res)

