class Solution:
    # O(E + Vlog(V)) time | O(E + V) space
    # where V is the number of vertices and E is the number of edges
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        edges = defaultdict(list)
        for source, destination in pairs:
            edges[source].append(destination)
            edges[destination].append(source)
        
        def dfs(vertex):
            characters.append(s[vertex])
            indices.append(vertex)
            visit.add(vertex)
            for adjacent in edges[vertex]:
                if adjacent not in visit:
                    dfs(adjacent)
        
        visit = set()
        res = [None for _ in range(len(s))]
        for vertex in range(len(s)):
            if vertex not in visit:
                characters, indices = [], []
                dfs(vertex)
                indices.sort()
                characters.sort()
                for index in range(len(characters)):
                    res[indices[index]] = characters[index]
                    
        return "".join(res)
