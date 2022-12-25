class Solution:
    # O((m+n)*log(n)) time | O(n) space 
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        
        ans = []

        for query in queries:
            index = bisect_right(nums, query)
            ans.append(index)

        return ans

