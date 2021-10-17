class Solution:
    # O(log(n)) time | O(1) space 
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            middle = (left + right) // 2
            if arr[middle + 1] < arr[middle] and arr[middle - 1] < arr[middle]:
                return middle
            elif arr[middle + 1] > arr[middle]:
                left = middle + 1
            else:
                right = middle - 1
        