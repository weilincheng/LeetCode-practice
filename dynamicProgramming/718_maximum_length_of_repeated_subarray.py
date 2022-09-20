class Solution:
    # O(m*n) time | O(n) space - where m is nums1.length and n is nums2.length
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        maxLen, prev = 0, [0 for _ in range(len(nums2) + 1)]
        
        for i in range(len(nums1)):
            cur = [0 for _ in range(len(nums2) + 1)]
            
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    cur[j + 1] = prev[j] + 1
                    maxLen = max(maxLen, cur[j + 1])
            
            prev = cur
        
        return maxLen

