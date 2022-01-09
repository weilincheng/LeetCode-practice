class Solution:
    # O(n) time | O(1) space - where n is the length of the input string
    def isRobotBounded(self, instructions: str) -> bool:
        dirX, dirY = 0, 1
        x, y = 0, 0
        for d in instructions:
            if d == "G":
                x, y = x + dirX, y + dirY     
            elif d == "L":
                dirX, dirY = -1 * dirY, dirX
            else:
                dirX, dirY = dirY, -1 * dirX
        """
        As long as the direction changes, it comes back to origin after at most three more iterations
        Prove: [dx, dy] + [dy, -dx] + [-dx, -dy] + [-dy, dx] = [0, 0] 
        """
        return (x, y) == (0, 0) or (dirX, dirY) != (0, 1)
    