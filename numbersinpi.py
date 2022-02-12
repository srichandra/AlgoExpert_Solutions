def numbersInPi(pi, numbers):
	n=len(pi)
    DP=[float('inf') for i in range(n+1)]
	for i in range(1,n+1):
		if (pi[0:i] in numbers):
			DP[i]=0
		if DP[i]!=float('inf'):
			if i==n:
				return DP[i]
			else:
				print('here',i)
				for j in range(i+1,n+1):
					print(pi[i:j])
					if pi[i:j] in numbers:
						print('here',pi[i:j])
						DP[j]=min(DP[j],1+DP[i])
						print(DP)
	return DP[-1] if not float('inf') else -1	
    pass
