def maxSumIncreasingSubsequence(array):
    # Write your code here.
	L=[each for each in array]
	for i in range(1,len(array)):
		for j in range(i):
			if array[j]<array[i]:
				if L[j]+array[i]>L[i]:
					L[i]=L[j]+array[i]
	maxi=float('-inf')
	for i in range(len(L)):
		if maxi<L[i]:
			maxi=L[i]
			maxind=i
	# backtrack
	i=maxind
	j=i-1
	result=[]
	result.append(array[i])
	while(j>=0):
		if(L[i]==L[j]+array[i]):
			result.append(array[j])
			i=j
			j=i-1
		else:
			j=j-1
	return [maxi,result[::-1]]
			
		
