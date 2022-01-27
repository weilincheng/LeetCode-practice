class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans, mask = 0, 0
        for i in range(30, -1, -1):
            mask |= 1 << i # Generate mask. Starting from 1000... (length is 31 bits)
            found = set([num & mask for num in nums]) # Traverse the nubmers 
            start = ans | 1 << i
            for pref in found:
                if start ^ pref in found:
                    ans = start
                    break
        return ans 
    