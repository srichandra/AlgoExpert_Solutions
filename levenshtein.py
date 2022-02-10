def levenshteinDistance(str1, str2):
    m=len(str1)
	n=len(str2)
	DP=[[0 for i in range(n+1)] for j in range(m+1)]
	for i in range(n+1):
		DP[0][i]=i # first string empty so insert as many characters as len of str2
	for i in range(m+1):
		DP[i][0]=i # second string empty so remove all characters as len of str1
	for i in range(1,m+1):
		for j in range(1,n+1):
			if str1[i-1]==str2[j-1]:
				DP[i][j]=DP[i-1][j-1]
			else:
				DP[i][j]=1+min(DP[i-1][j],DP[i][j-1],DP[i-1][j-1])
	return DP[-1][-1]
    pass
