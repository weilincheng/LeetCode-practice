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

    # Use an array to store the ways to reach certain stairs 
    # Start from the beginning of the stairs 
    # O(n) time | O(n) space - where n is the number of steps
    def climbStairs2(self, n: int) -> int:
        ways = [None for _ in range(n + 1)]
        ways[0], ways[1] = 1, 1
        for i in range(2, n + 1):
            ways[i] = ways[i - 1] + ways[i - 2]
        
        return ways[n]

    # Start from the beginning of the stairs 
    # O(n) time | O(1) space - where n is the number of steps
    def climbStairs3(self, n: int) -> int:
        one, two = 1, 1
        for i in range(2, n + 1):
            temp = two
            two = one + two
            one = temp 
        return two
