def indexEqualsValue(A):
    l=0
	r=len(A)
	while(l<r):		
		m=(l+r)//2
		if(A[m]==m):
			if A[m-1]==m-1:
				r=m
			else:
				return m
		elif A[m]<m:
			l=m+1
		else:
			r=m-1
	return -1
    pass
