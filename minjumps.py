def minNumberOfJumps(array):
    L=[float('inf') for i in range(len(array))]
	L[0]=0
	for i in range(1,len(array)):
		print(L)
		for j in range(i):
			if(array[j]>=(i-j)): # you can jump
				L[i]=min(L[i],1+L[j])
	
	return L[-1]
    pass
