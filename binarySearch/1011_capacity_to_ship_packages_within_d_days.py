class Solution:
    # O(nlog(s)) time | O(1) space
    # where n is the length of the array, s is the sum of the array
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(capacity):
            currSum, dayReq = 0, 0
            for weight in weights:
                currSum += weight
                if currSum > capacity:
                    dayReq += 1
                    currSum = weight
            return dayReq + 1 <= days
        
        left, right = max(weights), sum(weights)
        ans = right
        while left <= right:
            mid = left + (right - left) // 2
            if canShip(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans
