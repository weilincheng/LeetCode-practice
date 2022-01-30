class Solution:
    # O(n) time | O(1) space - where n is the length of the input array
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse_arr(left, right, arr):
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left, right = left + 1, right - 1
        
        k %= len(nums)
        
        reverse_arr(0, len(nums) - 1, nums)
        reverse_arr(0, k - 1, nums)
        reverse_arr(k, len(nums) - 1, nums)
