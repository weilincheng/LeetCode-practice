class Solution:
    # O(n) time | O(k) space - where n is the length of the input array
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        for idx, num in enumerate(nums):
            if num in seen:
                return True
            seen.add(num)
            
            if len(seen) > k:
                seen.remove(nums[idx - k])
        return False

