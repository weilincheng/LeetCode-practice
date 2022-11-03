class Solution:
    # O(n) time | O(n) space - where n is the number of words
    def longestPalindrome(self, words: List[str]) -> int:
        count = Counter(words)
        answer = 0
        central = False
        for word, wordCount in count.items():
            if word[0] == word[1]:
                if wordCount % 2 == 0:
                    answer += wordCount
                else:
                    answer += wordCount - 1
                    central = True
            elif word[0] < word[1]: # consider the pair only once
                answer += 2 * min(wordCount, count[word[::-1]])
        
        if central:
            answer += 1
        
        return 2 * answer 

