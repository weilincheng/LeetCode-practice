class Solution:
    # O(nlog(n)) time | O(n) space - where n is tasks.length
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for idx, task in enumerate(tasks):
            tasks[idx].append(idx)
        tasks.sort(key=lambda t: t[0], reverse=True)
        res, minHeap = [], []
        curTime = tasks[-1][0]

        while minHeap or tasks:
            while tasks and tasks[-1][0] <= curTime:
                _, processingTime, idx = tasks.pop()
                heapq.heappush(minHeap, (processingTime, idx))
            if minHeap:
                processingTime, idx = heapq.heappop(minHeap)
                curTime += processingTime
                res.append(idx)
            else:
                curTime = tasks[-1][0]
        return res

