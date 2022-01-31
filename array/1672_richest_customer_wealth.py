class Solution:
    # O(m * n) time | O(1) space - where m is the number of customers and n is the number of banks
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = 0
        for i in range(len(accounts)):
            maxWealth = max(maxWealth, sum(accounts[i]))
        return maxWealth
    