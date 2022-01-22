def isValidSubsequence(array, sequence):
    i=0
	j=0
	valid=True
	while((i<len(array))&(j<len(sequence))):
		if(sequence[j]==array[i]):
			j+=1
			i+=1
		else:
			i+=1
	if(j<len(sequence)):
		return False
	else:
		return True
    pass
