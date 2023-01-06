class Solution:
    # O(nlog(n)) time | O(n) space - where n is costs.length
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        for i, cost in enumerate(costs):
            coins -= cost
            if coins < 0:
                return i
        return len(costs)

