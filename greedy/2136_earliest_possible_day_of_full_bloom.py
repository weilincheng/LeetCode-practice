class Solution:
    # O(nlogn) time | O(n) space - where n is the length of the array
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        currTime, bloomTime = 0, []
        sortedTime = sorted([[growTime[i], plantTime[i]] for i in range(len(plantTime))], reverse=True)
        print(sortedTime)
        for [g, p] in sortedTime:
            bloomTime.append(currTime + g + p)
            currTime += p
        return max(bloomTime)