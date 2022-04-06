class Solution:
    # O(n + w^2) time | O(w) space
    # where n is the length of arr, and w is the maximum possible value of arr[i]
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = (10 ** 9) + 7
        ans, countNum = 0, [0] * 101
        for num in arr:
            countNum[num] += 1
        
        for i in range(len(countNum)):
            for j in range(i, len(countNum)):
                k = target - i - j
                if k < 0 or k >= len(countNum) or k < j: continue
                if not countNum[i] or not countNum[j] or not countNum[k]: continue
                if i == j == k:
                    ans += comb(countNum[i], 3)
                elif i == j != k:
                    ans += comb(countNum[j], 2) * countNum[k]
                elif i != j == k:
                    ans += comb(countNum[j], 2) * countNum[i]
                else:
                    ans += countNum[i] * countNum[j] * countNum[k]   

        return ans % MOD
