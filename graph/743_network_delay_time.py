class Solution:
    # O(N + Elog(N)) time | O(N + E) space
    # where N is the number of nodes and E is the number of edges
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for source, target, weight in times:
            edges[source].append((weight, target))
        
        visit = set()
        time = 0
        minHeap = [(0, k)]
        while minHeap:
            timeToSource, source = heapq.heappop(minHeap)
            if source not in visit:
                visit.add(source)
                time = timeToSource
            
            for timeToTarget, target in edges[source]:
                if target not in visit:
                    heapq.heappush(minHeap, (timeToSource + timeToTarget, target))
        
        return time if len(visit) == n else -1
            