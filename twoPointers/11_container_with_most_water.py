class Solution:
    # O(n) time | O(1) space - where n is the length of the input array
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1 
        ans = 0
        while l < r:
            ans = max(ans, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return ans
            