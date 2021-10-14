# Iterative solution 
# O(log(n)) time | O(1) space 
def binarySearch(array, target):
	left, right = 0, len(array) - 1
	while left <= right:
		mid = (left + right) // 2
		if target == array[mid]:
			return mid
		elif target > array[mid]:
			left = mid + 1
		else:
			right = mid - 1
		
	return -1

# Recursive solution
# O(log(n)) time | O(log(n)) space 
def binarySearch2(array, target):
	return binarySearchHelper(array, target, 0, len(array) - 1)

def binarySearchHelper(array, target, left, right):
	if left > right:
		return - 1
	middle = (left + right) // 2
	if target == array[middle]:
		return middle
	elif target < array[middle]:
		return binarySearchHelper(array, target, left, middle - 1)
	else:
		return binarySearchHelper(array, target, middle + 1, right)
