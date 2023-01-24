class Solution:
    # O(26n) time | O(26n) space 
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        res = [0] * n

        def dfs(node, parent):
            totalCount = Counter()
            totalCount[labels[node]] += 1
            for nei in graph[node]:
                if nei == parent: continue
                totalCount += dfs(nei, node)
            res[node] = totalCount[labels[node]]
            return totalCount
        
        dfs(0, None)
        return res

