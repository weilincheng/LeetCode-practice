class Solution:
    # O(nlog(n)) time | O(n) space - where n is the length of the input array
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        minHeap = []
        res = totalSpeed = 0
        MOD = 10 ** 9 + 7
        
        for e, s in sorted(zip(efficiency, speed), reverse = True):
            totalSpeed += s
            heapq.heappush(minHeap, s)
            
            if len(minHeap) > k:
                totalSpeed -= heapq.heappop(minHeap)
            
            res = max(res, totalSpeed * e) 
            
        return res % MOD

