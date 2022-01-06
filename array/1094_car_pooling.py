class Solution:
    # O(n) time | O(m) space - where n is the number of trips, m is the number of stops
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        STOPS = 1001
        path = [0] * STOPS
        for num, start, end in trips:
            path[start] += num
            path[end] -= num
        
        for i in range(STOPS):
            capacity -= path[i]
            if capacity < 0: return False
        
        return True