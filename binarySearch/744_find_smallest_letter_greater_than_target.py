class Solution:
    # O(log(n)) time | O(1) space - where n is the length of the array 
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        if target < letters[left] or target >= letters[right]:
            return letters[left]
        while left <= right:
            middle = (left + right) // 2
            if letters[middle] <= target:
                left = middle + 1
            else:
                right = middle - 1
        return letters[left]
    