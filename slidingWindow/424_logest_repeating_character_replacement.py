class Solution:
    # O(26n) time | O(26) space - where n is s.length
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26
        left = 0
        maxLen = 0
        for right in range(len(s)):
            freq[ord(s[right]) - ord('A')] += 1
            while (right - left + 1) - max(freq) > k:
                freq[ord(s[left]) - ord('A')] -= 1
                left += 1
            maxLen = max(maxLen, right - left + 1)
        return maxLen

