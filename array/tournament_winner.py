HOME_TEAM_WON = 1

# O(n) time | O(k) space
def tournamentWinner(competitions, results):
	currentBestTeam = ""
    scores = {currentBestTeam: 0}
	for idx, competition in enumerate(competitions):
		result = results[idx]
		homeTeam = competition[0]
		awayTeam = competition[1]
		
		if result == HOME_TEAM_WON: 
			 winningTeam = homeTeam 
		else: 
			 winningTeam = awayTeam 
		
		updateScores(winningTeam, 3, scores)
		
		if scores[winningTeam] > scores[currentBestTeam]:
			currentBestTeam = winningTeam
	
	return currentBestTeam
		
				
def updateScores(team, points, scores):
	if team not in scores: 
		scores[team] = 0
		
	scores[team] += points
