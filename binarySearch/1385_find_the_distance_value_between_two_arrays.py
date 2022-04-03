class Solution:
    # O(nlog(n) + mlog(n)) - where m is the length of arr1 and n is the length of arr2
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:        
        arr2.sort()
        
        def isValid(val):
            l, r = 0, len(arr2) - 1
            while l <= r:
                m = l + (r - l) // 2
                if abs(arr2[m] - val) <= d:
                    return False
                if val > arr2[m]:
                    l = m + 1
                else:
                    r = m - 1
            return True
        
        return sum(isValid(x) for x in arr1)
