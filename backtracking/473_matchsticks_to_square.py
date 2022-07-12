class Solution:
    # O(4^n) time | O(n) space - where n is matchsticks.length
    def makesquare(self, matchsticks: List[int]) -> bool:
        length = sum(matchsticks) // 4
        sides = [0] * 4
        
        if sum(matchsticks) / 4 != length: 
            return False
        
        matchsticks.sort(reverse=True)
        
        def backTrack(i):
            if i == len(matchsticks):
                return True
            
            for j in range(4):
                if sides[j] + matchsticks[i] <= length:
                    sides[j] += matchsticks[i]
                    if backTrack(i + 1):
                        return True
                    sides[j] -= matchsticks[i]
                    if sides[j] == 0: break
            return False
        
        return backTrack(0)                    
            
