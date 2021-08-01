# Time: O(nlog(n)) | Space O(1)
def nonConstructibleChange(coins):
	# Sort the array in place
	coins.sort()
	
	currentChangeCreated = 0
	for coin in coins:
		if coin > currentChangeCreated + 1:
			return currentChangeCreated + 1
		
		currentChangeCreated += coin
	
	return currentChangeCreated + 1
	