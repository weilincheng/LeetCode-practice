class Solution:
    # O(e + v) time | O(v) space
    # where E is the number of edges and v is the number of the vertexs 
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}
        
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            copy = Node(node.val)
            oldToNew[node] = copy
            
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy
                
        return dfs(node) if node else node
            