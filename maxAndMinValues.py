def findMaxMin(numbers):
	if max(numbers)== min(numbers):
		return [min(numbers)]
	return [min(numbers),max(numbers)]
	