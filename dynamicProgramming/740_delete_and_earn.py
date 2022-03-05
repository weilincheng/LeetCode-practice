class Solution:
    # O(nlog(n)) time | O(1) space - where n is the length of the array
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        nums = sorted(list(set(nums)))
        earn1, earn2 = 0, 0
        
        for i in range(len(nums)):
            currEarn = nums[i] * count[nums[i]]
            if i > 0 and nums[i] == nums[i - 1] + 1:
                temp = earn2
                earn2 = max(currEarn + earn1, earn2)
                earn1 = temp 
            else:
                earn1 = earn2
                earn2 += currEarn 
        
        return earn2
                