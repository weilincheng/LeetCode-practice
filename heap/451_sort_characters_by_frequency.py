class Solution:
    # Solution 1 - Dictionary + sort 
    # O(nlog(n)) Time | O(n) space - where n is the length of the input string
    def frequencySort(self, s: str) -> str:
        charCount, sortedArray = {}, []
        
        for char in s:
            charCount[char] = charCount.get(char, 0) + 1
        
        for key in sorted(charCount, key = charCount.get, reverse = True):
            sortedArray.append(key * charCount[key])
                
        return "".join(sortedArray)
    
    # Solution 2 - Dictionary + heap 

