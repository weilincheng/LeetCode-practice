class Solution:
    # O(n * 2^n) time | O(n * 2^n) space - where n is the length of the input array
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(path):
            if path[-1] == len(graph) - 1:
                res.append(path)
                return
            for child in graph[path[-1]]:
                dfs(path + [child])
                
        res = []
        dfs([0])
        return res
    