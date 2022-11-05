class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word):
        curNode = self
        for c in word:
            if c not in curNode.children:
                curNode.children[c] = TrieNode()
            curNode = curNode.children[c]
        
        curNode.isWord = True
    
    def removeWord(self, word):
        curNode = self
        parentNodesList = [] # (node, char)
        for c in word:
            parentNodesList.append((curNode, c))
            curNode = curNode.children[c]
        
        for parentNode, char in parentNodesList[::-1]:
            childNode = parentNode.children[char]
            if len(childNode.children) == 0:
                parentNode.children.pop(char)
            else:
                return

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)
        visit = set()
        ROWS, COLS = len(board), len(board[0])
        res = []
        
        def dfs(r, c, curWord, curNode):
            if r < 0 or r == ROWS or c < 0 or c == COLS or (r, c) in visit or board[r][c] not in curNode.children:
                return
            visit.add((r, c))
            curWord += board[r][c]
            curNode = curNode.children[board[r][c]]
            if curNode.isWord:
                res.append(curWord)
                curNode.isWord = False
                root.removeWord(curWord)
            
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                dfs(r + dr, c + dc, curWord, curNode)
            
            visit.remove((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, "", root)
        return res
    
