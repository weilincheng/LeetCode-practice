class Solution:
    # O(e + q * e) time | O(e) space
    # wehre e is the length of equations, and q is length of queries
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:               
        def dfs(start, end):
            if start == end: return 1.0
            visit.add(start)
            for nei in graphs[start]:
                if nei in visit:
                    continue
                d = dfs(nei, end)
                if d > 0: return d * graphs[start][nei]
            return -1.0
        
        graphs = defaultdict(dict)
        for idx, pair in enumerate(equations):
            start, end = pair
            graphs[start][end] = values[idx]
            graphs[end][start] = 1 / values[idx]
                    
        ans = []
        for query in queries:
            start, end = query
            if start not in graphs or end not in graphs: 
                ans.append(-1.0)
                continue
            visit = set()
            ans.append(float(dfs(start, end)))
        
        return ans
    