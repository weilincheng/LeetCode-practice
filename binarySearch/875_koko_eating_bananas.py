class Solution:
    # O(nlog(m)) time | O(1) space - where n is the length of the input array 
    # m is the largest number in the input array
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            speed = mid
            hourSpent = 0
            for pile in piles:
                hourSpent += math.ceil(pile / speed)
            if hourSpent <= h: 
                right = mid
            else:
                left = mid + 1
            
        return left
    