class Solution:
    # O(n) time | O(n) space - where n is num.length
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        res = []
        carry = 0
        while num or k:
            curNum = carry + k % 10
            if num:
                curNum += num.pop()
            carry = curNum // 10
            res.append(curNum % 10)
            k //= 10
        if carry:
            res.append(carry)
        return res[::-1]

