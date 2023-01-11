class Solution:
    # O(n) time | O(n) space
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visit = set()

        def dfs(node):
            visit.add(node)
            totalCost = 0
            for nextNode in graph[node]:
                if nextNode in visit: continue
                cost = dfs(nextNode)
                if cost > 0 or hasApple[nextNode]:
                    totalCost += cost + 2
            return totalCost
        return dfs(0)

