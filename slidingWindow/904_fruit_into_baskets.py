class Solution:
    # O(n) time | O(1) space - where n is fruits.length
    def totalFruit(self, fruits: List[int]) -> int:
        l, res = 0, 0
        count = {}
        
        for r in range(len(fruits)):
            count[fruits[r]] = count.get(fruits[r], 0) + 1
            while len(count) > 2:
                count[fruits[l]] -= 1
                if count[fruits[l]] == 0:
                    count.pop(fruits[l])
                l += 1
            res = max(res, r - l + 1)
        return res

