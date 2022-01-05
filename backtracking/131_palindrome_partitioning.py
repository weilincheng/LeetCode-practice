class Solution:
    # O(n * 2^n) time | O(n) space 
    def partition(self, s: str) -> List[List[str]]:
        
        def isPalindrome(s):
            left, right = 0, len(s) - 1
            while left < right:
                if s[left] != s[right]: return False
                left, right = left + 1, right - 1
            return True
        
        def dfs(start):
            if start >= len(s):
                result.append(currentList.copy())
            
            for end in range(start, len(s)):
                subString = s[start : end + 1]
                if isPalindrome(subString):
                    currentList.append(subString)
                    dfs(end + 1)
                    currentList.pop()

        result, currentList = [], []
        dfs(0)
        
        return result
