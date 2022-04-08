class KthLargest:
    # O(nlog(n) + mlog(k)) time | O(n) space 
    # where n is the length of nums, and m is the number of add operations 
    def __init__(self, k: int, nums: List[int]):
        self.minheap, self.k = nums, k
        heapq.heapify(self.minheap)
        while len(self.minheap) > self.k:
            heapq.heappop(self.minheap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)
        if len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]
