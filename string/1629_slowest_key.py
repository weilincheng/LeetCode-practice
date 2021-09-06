class Solution:
    # O(n) time | O(1) space - where n is the length of the input list
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        maxDuration, startTime, slowestKey = 0, 0, ''
        for i in range(len(releaseTimes)):
            pressTime = releaseTimes[i] - startTime
            if pressTime > maxDuration:
                maxDuration = pressTime
                slowestKey = keysPressed[i]
            elif pressTime == maxDuration and keysPressed[i] > slowestKey:
                slowestKey = keysPressed[i]
            startTime = releaseTimes[i]
        return slowestKey
