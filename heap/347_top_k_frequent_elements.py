class Solution:
    # O(klog(n)) time | O(n) space - where n is the length of the input array
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        
        count = Counter(nums)
        minheap = [(-val, key) for key, val in count.items()]
        heapq.heapify(minheap)

        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(minheap)[1])
    
        return ans
    