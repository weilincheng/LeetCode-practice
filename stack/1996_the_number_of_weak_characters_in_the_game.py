class Solution:
    # O(nlog(n)) time | O(n) space - where n is the length of the input array
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key = lambda k: (k[0], -k[1]))
        stack = []
        res = 0
        
        for character in properties:
            while stack and stack[-1] < character[1]:
                stack.pop()
                res += 1
            stack.append(character[1])
            
        return res

