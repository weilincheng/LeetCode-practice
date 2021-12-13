class Solution:
    # O(n) time | O(1) space - where n is the length of the input string
    def maxPower(self, s: str) -> int:
        max_count = count = 1
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                count += 1
            else:
                count = 1
            max_count = max(max_count, count)
                
        return max_count
    