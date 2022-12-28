class Solution:
    # O(klog(n)) time | O(n) space - where n is piles.length
    def minStoneSum(self, piles: List[int], k: int) -> int:
        maxHeap = []
        for stones in piles:
            heapq.heappush(maxHeap, -stones)
        
        for _ in range(k):
            stones = -heapq.heappop(maxHeap)
            stones -= stones // 2
            heapq.heappush(maxHeap, -stones)
        
        return -sum(maxHeap)

