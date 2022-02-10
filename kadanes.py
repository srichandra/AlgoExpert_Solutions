def kadanesAlgorithm(array):
    maxsofar=float('-inf')
    curr=0
	for i in range(len(array)):
		curr+=array[i]
		if curr>=maxsofar:
			maxsofar=curr
		if curr<0:
			curr=0
		print(curr,maxsofar)
	return maxsofar
    pass
