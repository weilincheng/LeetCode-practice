class Solution:
    # O(N+Q) time | O(Q) space - where N is nums.length and Q is queries.length
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evenSum = sum(x for x in nums if x % 2 == 0)
        ans = []
        
        for val, index in queries:
            if nums[index] % 2 == 0:
                evenSum -= nums[index]
            nums[index] += val
            if nums[index] % 2 == 0:
                evenSum += nums[index]
            ans.append(evenSum)
        
        return ans
    
