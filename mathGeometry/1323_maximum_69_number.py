class Solution:
    # O(n) time | O(1) space - where n is the number of digits
    def maximum69Number (self, num: int) -> int:
        curDigit = 0
        firstSix = -1
        numCopy = num
        while numCopy:
            if numCopy % 10 == 6:
                firstSix = curDigit
            numCopy //= 10
            curDigit += 1
        
        return num if firstSix == -1 else num + 3 * 10 ** firstSix

