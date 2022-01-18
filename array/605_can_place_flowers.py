class Solution:
    # O(n) time | O(1) space 
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            prev = 0 if i == 0 else flowerbed[i - 1]
            nex = 0 if i == len(flowerbed) - 1 else flowerbed[i + 1]
            if flowerbed[i] == 0 and prev == 0 and nex == 0:
                flowerbed[i] = 1
                n -= 1    
        return n <= 0
