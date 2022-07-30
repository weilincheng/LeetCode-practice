class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        words2Count = Counter()
        for word in words2:
            words2Count |= Counter(word)
        
        return [word for word in words1 if not words2Count - Counter(word)]

