class Solution:
    # O(nlog(n)) time | O(n) space - where n is the length of the input array
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minDiff = arr[1] - arr[0]
        res = []
        for i in range(len(arr) - 1):
            currentDiff = arr[i + 1] - arr[i]
            if currentDiff < minDiff:
                res = [[arr[i], arr[i + 1]]]
                minDiff = currentDiff
            elif currentDiff == minDiff:
                res.append([arr[i], arr[i + 1]])
        return res
