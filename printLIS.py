def longestIncreasingSubsequence(arr):
    DP=[1 for i in range(len(arr))]
    for i in range(1,len(arr)):
		for j in range(0,i):
            if (arr[j]<arr[i]) and (DP[i]<DP[j]+1):
				DP[i]=DP[j]+1
    maximum = 0
	maxidx=-1
    for i in range(len(arr)):
		if DP[i]>maximum:
			maximum=DP[i]
			maxidx=i
	i=maxidx
	j=maxidx-1
	result=[]
	result.append(arr[i])

	while(j>=0):
		print(i,j,result)
		if (arr[j]<arr[i]) and (DP[i]==DP[j]+1):
			result.append(arr[j])
			i=j
			j=i-1
		else:
			j=j-1
	return result[::-1]
    # back track
