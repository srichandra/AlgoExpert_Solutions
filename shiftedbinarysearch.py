def shiftedBinarySearch(A, target):
	l=0
	r=len(A)-1
    while(l<=r):
		m=(l+r)//2
		if(A[m]==target):
			return m
		elif(A[l]<=A[m]): # l to m is sorted
			if(A[l]<=target<=A[m]):
				r=m-1
			else:
				l=m+1
		else: # m to h is sorted
			if A[m]<=target<=A[r]:
				l=m+1
			else:
				r=m-1
	return -1
    pass
