class Solution:
    # O(n) time | O(1) space - where n is the length of the input array
    def equationsPossible(self, equations: List[str]) -> bool:
        
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            
            return parent[x]
        
        parent = [i for i in range(26)]
        
        for e in equations:
            if e[1] == "=":
                parent[find(ord(e[0]) - ord('a'))] = find(ord(e[3]) - ord('a'))
        
        for e in equations:
            if e[1] == "!" and find(ord(e[0]) - ord('a')) == find(ord(e[3]) - ord('a')):
                return False
        
        return True
    
