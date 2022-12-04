class Solution:
    # O(n) time | O(1) space - where n is the length of the input array
    def minimumAverageDifference(self, nums: List[int]) -> int:
        N = len(nums)
        best, bestIdx = float('inf'), -1
        prefixSum = 0 
        suffixSum = sum(nums)
        
        for i in range(N):
            prefixSum += nums[i]
            suffixSum -= nums[i]
            prefixCount = i + 1 
            suffixCount = N - i - 1 if i < N - 1 else 1
            
            avgDiff = abs(prefixSum // prefixCount - suffixSum // suffixCount) 
            if avgDiff < best:
                best = avgDiff
                bestIdx = i

        return bestIdx

