def subarraySort(A):
	mini=float('inf')
	maxi=float('-inf')
    for i in range(len(A)):
		if isout(A,i,A[i]):
			if A[i]<mini:
				mini=A[i]
			if A[i]>maxi:
				maxi=A[i]
	if mini==float('inf'):
		return [-1,-1]
	i=0
	while(A[i]<=mini):
		i+=1
	minind=i	
	i=len(A)-1
	while(A[i]>=maxi):
		i-=1
	maxind=i
		
	return [minind,maxind]
def isout(A,i,num):
	if(i==0):
		return num>A[i+1]
	if i==len(A)-1:
		return num<A[i-1]
	return num>A[i+1] or num<A[i-1]
