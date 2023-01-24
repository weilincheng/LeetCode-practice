class Solution:
    # O(n*m^2) time | O(26 * m + n) space 
    # where n is the lenght of wordList and the m is the length the word
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: 
            return 0
        
        neighbor = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                neighbor[pattern].append(word)
        
        visited = set([beginWord])
        q = deque([beginWord])
        result = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord: 
                    return result 
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1:]
                    for neighborWord in neighbor[pattern]:
                        if neighborWord not in visited:
                            visited.add(neighborWord)
                            q.append(neighborWord)
            result += 1
        return 0
    