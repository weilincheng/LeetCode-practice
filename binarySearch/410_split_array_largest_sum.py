class Solution:
    # O(nlog(s)) | O(1) space
    # where n is the length of the array and s is sum of integers in the array
    def splitArray(self, nums: List[int], m: int) -> int:
        def minSubarraysRequired(maxSumAllowed):
            currSum = 0
            splitsRequired = 1
            
            for element in nums:
                if currSum + element <= maxSumAllowed:
                    currSum += element
                else:
                    splitsRequired += 1
                    currSum = element
            
            return splitsRequired
        
        left, right = max(nums), sum(nums)
        while left <= right:
            maxSumAllowed = (left + right) // 2
            
            if minSubarraysRequired(maxSumAllowed) <= m:
                right = maxSumAllowed - 1
                minimumLargestSplitSum = maxSumAllowed
            else:
                left = maxSumAllowed + 1
        
        return minimumLargestSplitSum
    