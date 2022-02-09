class Solution:
    # O(n) time | O(n) space - where n is the length of the input array
    def findPairs(self, nums: List[int], k: int) -> int:
        count, result = {}, 0
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for num in count:
            if (k == 0 and count[num] > 1) or (k > 0 and num + k in count):
                result += 1
        return result
    