class Solution:
    # O(nlog(n)) time | O(n) space - where n is the length of the input array
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            first, second = heapq.heappop(stones), heapq.heappop(stones)
            if first < second:
                heapq.heappush(stones, first - second)
        
        stones.append(0)
        return abs(stones[0])
    