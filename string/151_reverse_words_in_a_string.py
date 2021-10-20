class Solution:
    # O(n) time | O(n) space 
    def reverseWords(self, s: str) -> str:
        array = list(s)
        self.reverseString(array, 0, len(array) - 1)
        self.reverseWord(array)
        word = self.trimSides(array)
        res = self.trimSpace(word)
        return ''.join(res)

    def reverseString(self, array, left, right):
        while left < right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
        return array
    
    def reverseWord(self, array):
        left, right = 0, 0
        while right < len(array):
            while right < len(array) and not array[right].isspace():
                right += 1
            self.reverseString(array, left, right - 1)
            right += 1
            left = right
        return array
    
    def trimSides(self, array):
        if ''.join(array).isspace():
            return []
        left, right = 0, len(array) - 1
        while left < right and array[left].isspace():
            left += 1
        while left < right and array[right].isspace():
            right -= 1
        return array[left:right + 1]
    
    def trimSpace(self, word):
        if not word: 
            return []
        res = [word[0]]
        for i in range(1, len(word)):
            if res[-1].isspace() and word[i].isspace(): 
                continue
            res.append(word[i])
        return res
