class Solution:
    # O(n) time | O(n) space - where n is temperatures.length
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for idx, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prevIdx = stack.pop()
                ans[prevIdx] =  idx - prevIdx
            stack.append(idx)
        return ans

