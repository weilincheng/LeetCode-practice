class Solution:
    # O(n) time | O(n) space - where n is words.length
    def minimumLengthEncoding(self, words: List[str]) -> int:
        longestSuffix = set(words)
        for word in words:
            for i in range(1, len(word)):
                if word[i:] in longestSuffix:
                    longestSuffix.remove(word[i:])
            
        return sum(len(word) + 1 for word in longestSuffix)

