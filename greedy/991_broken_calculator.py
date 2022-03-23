class Solution:
    # O(log(target - startValue)) time | O(1) space
    def brokenCalc(self, startValue: int, target: int) -> int:
        if startValue >= target: return startValue - target
        count = 0
        while target != startValue:
            if target % 2 or target < startValue:
                target += 1
            else:
                target /= 2
            count += 1
        return count
        