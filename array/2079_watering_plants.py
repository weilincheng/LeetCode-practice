class Solution:
    # O(n) time | O(1) space - where n is the length of the input array
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        ans, currentCap = 0, capacity
        for i, water in enumerate(plants):
            if currentCap < water:
                ans += 2 * i
                currentCap = capacity
            ans += 1
            currentCap -= water
        return ans
    