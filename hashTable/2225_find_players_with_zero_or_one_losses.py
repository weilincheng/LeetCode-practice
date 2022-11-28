class Solution:
    # O(nlog(n)) time | O(n) space - where n is the number of matches
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        answer = [[], []]
        lossesCount = {}
        
        for winner, loser in matches:
            lossesCount[loser] = lossesCount.get(loser, 0) + 1
            lossesCount[winner] = lossesCount.get(winner, 0)
        
        for player, count in sorted(lossesCount.items()):
            if count < 2:
                answer[count].append(player)

        return answer
    
