class Solution:
    # O(n) time | O(5) space - where n is the input integer
    def countVowelPermutation(self, n: int) -> int:
        dp = {"a": 1, "e": 1, "i": 1, "o": 1, "u": 1}
        mod = 10 ** 9 + 7
        for _ in range(n - 1):
            nextDP = {}
            nextDP["a"] = (dp["e"] + dp["i"] + dp["u"]) % mod
            nextDP["e"] = (dp["a"] + dp["i"]) % mod
            nextDP["i"] = (dp["e"] + dp["o"]) % mod
            nextDP["o"] = (dp["i"]) % mod
            nextDP["u"] = (dp["i"] + dp["o"]) % mod
            dp = nextDP
        return (dp["a"] + dp["e"] + dp["i"] + dp["o"] + dp["u"]) % mod

