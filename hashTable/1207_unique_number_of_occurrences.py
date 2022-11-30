class Solution:
    # O(n) time | O(n) space - where n is the length of the input array
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = Counter(arr)
        seenFreq = set()
        for count in freq.values():
            if count in seenFreq:
                return False
            seenFreq.add(count)
        
        return True
