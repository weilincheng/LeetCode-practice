class Solution:
    def intToRoman(self, num: int) -> str:
        intList = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romanList = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        
        res = []
        for i in range(len(intList)):
            if intList[i] <= num:
                count = num // intList[i]
                num %= intList[i]
                res.append(romanList[i] * count)
                
        return "".join(res)

