def knapsackProblem(items, capacity):
    # Write your code here.
    # return [
    #   10, // total value
    #   [1, 2], // item indices
    # ]
	N=len(items)
	W=capacity
	DP=[[0 for x in range(0,W+1)] for y in range(0,N+1)] # (N+1)x(W+1)
	for i in range(N+1):		
		for j in range(W+1):
			if(i==0) or (j==0):
				DP[i][j]=0
			else:				
				currval=items[i-1][0]
				currwt=items[i-1][1]
				if(currwt>j): # item heavier than current capacity, then dont include it
					DP[i][j]=DP[i-1][j]
				else:
					V0=DP[i-1][j]
					V1=DP[i-1][j-currwt]+currval
					DP[i][j]=max(V0,V1)
	# DP has values filled
	# lets backtrack
	path=[]
	j=W
	for i in range(N,0,-1):
		if DP[i][j]==DP[i-1][j]:
			continue
		else:
			currval=items[i-1][0]
			currwt=items[i-1][1]
			if DP[i][j]==DP[i-1][j-currwt]+currval:
				j=j-currwt
				path.append(i-1)
	path.sort()
	final=[DP[N][W],path]
	return final
    pass
