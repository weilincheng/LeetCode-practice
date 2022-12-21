class Solution:
    # O(V+E) time | O(V+E) space
    # where V is the number of vertices and E is the number of edges
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        
        colors = [0] * (n + 1)

        def coloring(node, color):
            colors[node] = color
            for nei in graph[node]:
                if colors[nei] == color:
                    return False
                if colors[nei] == 0 and not coloring(nei, -color):
                    return False
            return True

        for i in range(1, n + 1):
            if colors[i] == 0 and not coloring(i, 1):
        o        return False
        return True

