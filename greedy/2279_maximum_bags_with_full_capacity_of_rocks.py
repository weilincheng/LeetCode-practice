class Solution:
    # O(nlog(n)) time | O(n) space - where n is rocks.length
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        count = sorted(cap - rock for cap, rock in zip(capacity, rocks))[::-1]
        while count and additionalRocks > 0 and count[-1] <= additionalRocks:
            additionalRocks -= count.pop()
        return len(rocks) - len(count)

