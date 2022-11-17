class Solution:
    # O(1) time | O(1) space
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        xOverlap = min(ax2, bx2) - max(ax1, bx1)
        yOverlap = min(ay2, by2) - max(ay1, by1)
        totalArea = (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1)
        
        if xOverlap > 0 and yOverlap > 0:
            return totalArea - xOverlap * yOverlap
        
        return totalArea
    
