def maxProfitWithKTransactions(prices, k):
	if len(prices)==0 or len(prices)==1:
		return 0
	n=len(prices)
	DP=[[0 for i in range(n)] for j in range(k+1)]
	for t in range(1,k+1):
		for i in range(1,n):
			DP[t][i]=DP[t][i-1] # no activity on ith day
			for j in range(0,i):
				DP[t][i]=max(DP[t][i],(prices[i]-prices[j]+DP[t-1][j]))
	return DP[-1][-1]
			
