class Solution:
    # Store the frequency of all the five characters in the give string text
    # Find the potential of each of the five characters
    # Return the minimum potential of the five characters
    def maxNumberOfBalloons(self, text: str) -> int:
        bCount = aCount = lCount = oCount = nCount = 0
        for char in text:
            if char == 'b':
                bCount += 1
            elif char == 'a':
                aCount += 1
            elif char == 'l':
                lCount += 1
            elif char == 'o':
                oCount += 1
            elif char == 'n':
                nCount += 1
        
        lCount = lCount // 2
        oCount = oCount // 2
        return min(bCount, aCount, lCount, oCount, nCount)
