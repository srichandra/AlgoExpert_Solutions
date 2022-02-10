def minNumberOfCoinsForChange(n, denoms):
    DP=[float('inf') for i in range(n+1)]
	DP[0]=0
	for denom in denoms:
		for i in range(1,n+1):
			if denom<=i:
				DP[i]=min(DP[i],1+DP[i-denom])
	
	return DP[-1] if DP[-1]!=float('inf') else -1
	
    pass
