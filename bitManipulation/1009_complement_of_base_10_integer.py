class Solution:
    # O(log(n)) time | O(1) space
    def bitwiseComplement(self, n: int) -> int:
        x = 1
        while n > x: x = x * 2 + 1
        retrun x - n
