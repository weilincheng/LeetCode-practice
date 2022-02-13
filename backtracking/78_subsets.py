class Solution:
    # O(n * 2^n) time | O(n * 2^n) space - where n is the length of the input array
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        
        def dfs(i):
            if i == len(nums):
                result.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i + 1)        
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        
        return result
    