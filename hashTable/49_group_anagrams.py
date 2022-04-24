class Solution:
    # O(m * n) time | O(m) space - where m is the number of words 
    # and n is the length of the longest word
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            anagram[tuple(count)].append(s)
        
        return anagram.values()
