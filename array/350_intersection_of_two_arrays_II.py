class Solution:
    # Use dict to store the appearance of number in nums1
    # Check whether these numbers in nums2
    # O(n) time | O(n) space - where n is the length of the input array
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seenNum = {}
        intersectionArray = []
        for num in nums1:
            seenNum[num] = seenNum.get(num, 0) + 1
            
        for num in nums2:
            if num in seenNum and seenNum[num] > 0:
                intersectionArray.append(num)
                seenNum[num] -= 1
        return intersectionArray 
        
    