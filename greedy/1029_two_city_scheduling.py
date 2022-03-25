class Solution:
    # O(nlog(n)) time | O(n) space - where n is the length of the array
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda k: k[0] - k[1])
        res = 0
        for i in range(len(costs)):
            if i < len(costs) // 2:
                res += costs[i][0]
            else:
                res += costs[i][1]
        return res
