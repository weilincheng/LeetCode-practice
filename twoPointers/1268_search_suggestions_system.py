class Solution:
    # O(nlog(n) + n + m) time | O(1) spcae
    # where n is products.length and m is searchWord.length
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []
        products.sort()
        l, r = 0, len(products) - 1
        for i in range(len(searchWord)):
            c = searchWord[i]
            
            while l <= r and (len(products[l]) <= i or products[l][i] != c):
                l += 1
            while l <= r and (len(products[r]) <= i or products[r][i] != c):
                r -= 1
            
            remain = r - l + 1
            res.append([])
            for j in range(min(3, remain)):
                res[-1].append(products[l + j])
        
        return res

