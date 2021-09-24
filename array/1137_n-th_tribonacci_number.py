class Solution:
    # Create an array with size of three to store the required value to count tribonacci number
    # O(n) time | O(1) space 
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        lastThree = [0, 1, 1]
        counter = 3
        while counter <= n:
            nextTri = lastThree[0] + lastThree[1] + lastThree[2]
            lastThree[0] = lastThree[1]
            lastThree[1] = lastThree[2]
            lastThree[2] = nextTri
            counter += 1

        return lastThree[2]
    