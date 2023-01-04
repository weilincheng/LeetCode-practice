class Solution:
    # O(n) time | O(n) space - where n is the tasks.length
    def minimumRounds(self, tasks: List[int]) -> int:
        levelCount = Counter(tasks)
        res = 0
        for count in levelCount.values():
            if count == 1:
                return -1
            res += (count + 2) // 3
        return res
