class Solution:
    # O(klog(n)) time | O(1) space 
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i, num in enumerate(nums):
            nums[i] = -num
        
        heapq.heapify(nums)
        while k > 0:
            ans = heapq.heappop(nums)
            k -= 1
        
        return -ans
        