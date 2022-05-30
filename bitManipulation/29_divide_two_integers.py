class Solution:
    # O(log(n)) time | O(1) space - where n is the value of dividend
    def divide(self, dividend: int, divisor: int) -> int:
        sign = (dividend < 0) == (divisor < 0)
        a, b, res = abs(dividend), abs(divisor), 0
        while a >= b:
            x = 0
            while a >= b << (x + 1):
                x += 1
            res += 1 << x
            a -= b << x
        return min(res if sign else -res, 2147483647)
