class Solution:
    # O((e+n)*k) time | O(n) space - where e is the flights.length
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for _ in range(k + 1):
            tempPrices = prices.copy()
            for s, d, price in flights:
                if prices[s] == float("inf"):
                    continue
                if prices[s] + price < tempPrices[d]:
                    tempPrices[d] = prices[s] + price
            prices = tempPrices
        return prices[dst] if prices[dst] != float("inf") else -1

