class Solution:
    # Use DP to calculate the number of ways after 1 and 2 steps. 
    # Start from the end of the stairs (bottom up approach)
    # O(n) time | O(1) space - where n is the number of stairs  
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
            
        return one
