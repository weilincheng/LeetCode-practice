class Solution:
    # O(n) time | O(1) space - where n is the length of the input array
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1
        start = totalGas = 0
        for i in range(len(gas)):
            totalGas += gas[i] - cost[i]
            if totalGas < 0:
                totalGas = 0
                start = i + 1
        
        return start
    