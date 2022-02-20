class Solution:
    # O(nlog(n)) time | O(n) space - where n is the length of the input array
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda k : (k[0], -k[1]))
        result = len(intervals)
        lastStart, lastEnd = intervals[0]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start == lastStart or end <= lastEnd:
                result -= 1
            else:
                lastStar, lastEnd = start, end
        
        return result 
