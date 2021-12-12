class Solution:
    # O(n * sum(nums)) time | O(n * sum(nums)) space
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2: return False
        target = sum(nums) // 2
        dp = {0}
        for num in nums:
            nextDP = set()
            for t in dp:
                if t + num == target: return True
                nextDP.add(t + num)
                nextDP.add(t)
            dp = nextDP
        return False
    