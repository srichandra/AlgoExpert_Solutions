def isMonotonic(array):
    isnondecreasing=True
	isnonincreasing=True
	for i in range(1,len(array)):
		if array[i] < array[i-1]:
			isnondecreasing= False
		if array[i] > array[i-1]:
			isnonincreasing = False
	return isnondecreasing or isnonincreasing
    
    pass
