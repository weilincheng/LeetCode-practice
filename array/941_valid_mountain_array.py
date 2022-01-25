class Solution:
    # O(n) time | O(1) space - where n is the length of the input array
    def validMountainArray(self, arr: List[int]) -> bool:
        i, n = 0, len(arr)
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1

        if i == 0 or i == n - 1:
            return False
        
        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1
        
        return i == n - 1
