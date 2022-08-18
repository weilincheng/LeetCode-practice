class Solution:
    # O(nlog(n)) time | O(n) space 
    def minSetSize(self, arr: List[int]) -> int:
        count = Counter(arr)
        halfLen = len(arr) // 2
        res, setCount = 0, 0
        for freq in sorted(count.values(), reverse=True):
            setCount += freq
            res += 1
            if setCount >= halfLen:
                return res
            
