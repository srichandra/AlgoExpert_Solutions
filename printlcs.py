def longestCommonSubsequence(str1, str2):
    N1=len(str1)
	N2=len(str2)
	if N1==0 or N2==0:
		return []
	L=[[0 for x in range(N2+1)] for y in range(N1+1)]
	for i in range(N1+1):
		for j in range(N2+1):
			if (i==0) or (j==0):
				L[i][j]=0
			elif str1[i-1]==str2[j-1]:
				L[i][j]=1+L[i-1][j-1]
			else:
					M0=L[i-1][j]
					M1=L[i][j-1]
					L[i][j]=max(M0,M1)
    
	# backtrack
	i=N1
	j=N2

	result=[]
	while(i>0 and j>0):
		if str1[i-1] == str2[j-1]:
    		result.append(str1[i-1])
            i-=1
            j-=1
        elif L[i-1][j] > L[i][j-1]:
            i-=1
        else:
            j-=1
	return result[::-1]
	
