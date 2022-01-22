def mergeSort(array):
	def mergeSortnew(a,l,r):
		if(l<r):
			m=l+(r-l)//2
			mergeSortnew(a,l,m)
			mergeSortnew(a,m+1,r)
			merge(a,l,m,r)
	def merge(a,l,m,r):
		n1=m-l+1
		n2=r-m
		a1=[0]*n1
		a2=[0]*n2
		for i in range(n1):
			a1[i]=a[l+i]
		for j in range(n2):
			a2[j]=a[m+1+j]
		i=0
		j=0
		k=l
		while((i<n1) and (j<n2)):
			if(a1[i]<a2[j]):
				a[k]=a1[i]
				i+=1
				k+=1
			else:
				a[k]=a2[j]
				j+=1
				k+=1
		while(i<n1):
			a[k]=a1[i]
			i+=1
			k+=1
		while(j<n2):
			a[k]=a2[j]
			j+=1
			k+=1
    l=0
	r=len(array)-1
	mergeSortnew(array,l,r)
	return array
    pass
