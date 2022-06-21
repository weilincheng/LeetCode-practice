class Solution:
    # O(nlog(L)) time | O(L) space - where L is ladders.length
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        N = len(heights)
        minHeap = []
        for i in range(1, N):
            diff = heights[i] - heights[i - 1]
            if diff <= 0: 
                continue
            heapq.heappush(minHeap, diff)
            if len(minHeap) <= ladders:
                continue
            bricks -= heapq.heappop(minHeap)
            if bricks < 0:
                return i - 1
        return N - 1
                
