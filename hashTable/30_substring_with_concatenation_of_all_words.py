class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordFreq = Counter(words)
        wordLen = len(words[0])
        wordCount = len(words)
        substringLen = wordLen * wordCount
        res = []
        for i in range(len(s) - substringLen + 1):
            seen = defaultdict(int)
            for j in range(i, i + substringLen, wordLen):
                curWord = s[j : j + wordLen]
                if curWord in wordFreq:
                    seen[curWord] += 1
                    if seen[curWord] > wordFreq[curWord]:
                        break
                else:
                    break
            if seen == wordFreq:
                res.append(i)
        return res

