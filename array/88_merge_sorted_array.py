class Solution:
    # O(n) time | O(1) space - where n is the length of input nums1
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        mergedIdx = len(nums1) -1 
        nums1Idx = m - 1
        nums2Idx = n - 1
        while nums2Idx >= 0:
            if nums1Idx >= 0 and nums1[nums1Idx] > nums2[nums2Idx]:
                nums1[mergedIdx] = nums1[nums1Idx]
                nums1Idx -= 1
            else:
                nums1[mergedIdx] = nums2[nums2Idx]
                nums2Idx -= 1
            mergedIdx -= 1
