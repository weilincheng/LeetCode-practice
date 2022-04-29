class Solution:
    # O(V+E) time | O(V) space
    # where V is the number of vertices, and E is the number of edges
    def isBipartite(self, graph: List[List[int]]) -> bool:
        N = len(graph)
        colors = [None for _ in range(N)]
        
        def coloring(color, node):
            if colors[node]:
                return colors[node] == color
            
            colors[node] = color
            for nei in graph[node]:
                if not coloring(-color, nei):
                    return False
            return True
        
        for i in range(N):
            if not colors[i] and not coloring(1, i):
                return False
        
        return True
