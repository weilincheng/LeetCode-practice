class Solution:
    # O(nlog(k)) time | O(n) space - where n is the length of the input array
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        return heapq.nsmallest(k, count, key = lambda word : (-count[word], word))

