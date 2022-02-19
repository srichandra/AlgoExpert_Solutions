def searchForRange(A, target):
    res=[-1,-1]
	l=0
	r=len(A)
	while(l<=r):
		m=(l+r)//2
		if A[m]==target:
			if m==0:
				res[0]=m
				break
			if A[m-1]!=A[m]:
				res[0]=m
				break
			else:
				r=m
		elif A[m]<target:
			l=m+1
		else:
			r=m-1
	
	l=0
	r=len(A)
	while(l<=r):
		m=(l+r)//2
		if A[m]==target:
			if m==len(A)-1:
				res[1]=m
				break
			if A[m+1]!=A[m]:
				res[1]=m
				break
			else: #A[m+1]
				l=m+1
		elif A[m]<target:
			l=m+1
		else:
			r=m-1
	return res
    pass
