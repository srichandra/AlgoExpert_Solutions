def numberOfWaysToTraverseGraph(width, height):
    DP=[[0 for i in range(width)] for j in range(height)]
	for i in range(1,width):
		DP[0][i]=1
	for j in range(1,height):
		DP[j][0]=1
	for i in range(1,height):
		for j in range(1, width):
			DP[i][j]=DP[i-1][j]+DP[i][j-1]
	return DP[-1][-1]
    return 0
