def numberOfWaysToMakeChange(n, denoms):
    DP=[0 for i in range(n+1)]
	DP[0]=1
	for denom in denoms:
		for i in range(1,n+1):
			if denom<=i:
				DP[i]=DP[i]+DP[i-denom]
	return DP[n]
    pass
