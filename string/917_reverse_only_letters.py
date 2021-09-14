class Solution:
    # Use two pointers to iterate the string
    # Move to the next one if encounters non alphabet character
    # O(n) time | O(n) space - where n is the length of the input string
    def reverseOnlyLetters(self, s: str) -> str:
        left, right = 0, len(s) - 1
        answer = [None for _ in range(len(s))]
        while left <= right:
            if s[left].isalpha() and s[right].isalpha():
                answer[left], answer[right] = s[right], s[left]
                left += 1
                right -= 1
            elif not s[left].isalpha():
                answer[left] = s[left]
                left += 1
            elif not s[right].isalpha():
                answer[right] = s[right]
                right -= 1
        return ''.join(answer)
                