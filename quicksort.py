def partition(A,l,r):
	key=A[r]
	i=0
	j=0
	while(j<r):
		if(A[j]<=key):
			A[j],A[i]=A[i],A[j]
			i+=1
		j+=1
	A[i],A[r]=A[r],A[i]
	return i
def quickSortutil(A,l,r):
	if(l<r):
		k=partition(A,l,r)
		quickSortutil(A,l,k-1)
		quickSortutil(A,k+1,r)
def quickSort(A):
	quickSortutil(A,0,len(A)-1)
	return A
	
	
    pass
