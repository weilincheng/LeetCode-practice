class Solution:
    # O(n) time | O(1) space - where n is the length of the input string
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        l = r = 0
        
        while r < len(colors): 
            curMax = curTotal = 0
            
            while r < len(colors) and colors[l] == colors[r]:
                curTotal += neededTime[r] 
                curMax = max(curMax, neededTime[r])
                r += 1

            res += curTotal - curMax
            l = r
        
        return res

