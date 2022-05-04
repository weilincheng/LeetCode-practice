class Solution:
    # O(n) time | O(n) space - where n is the length of the input array
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = {}
        ans = 0
        for num in nums:
            potentialMatch = k - num
            if potentialMatch in count:
                count[potentialMatch] -= 1
                ans += 1
                if count[potentialMatch] == 0:
                    count.pop(potentialMatch)
            else:
                count[num] = count.get(num, 0) + 1
        
        return ans
    