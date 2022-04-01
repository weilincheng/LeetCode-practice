class Solution:
    # O(n) time | O(n) space - where n is the length of s
    def reverseVowels(self, s: str) -> str:
        ans = list(s)        
        left, right = 0, len(s) - 1
        vowels = set(list('aeiouAEIOU'))
        while left < right:
            while left < right and ans[left] not in vowels:
                left += 1
            while left < right and ans[right] not in vowels:
                right -= 1
            ans[left], ans[right] = ans[right], ans[left]
            left, right = left + 1, right - 1
        
        return "".join(ans)
