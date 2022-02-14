def heapSort(array):
    def heapify(array,i,end):
		l=2*i+1
		while(l<=end):
			r=2*i+2 if 2*i+2<=end else -1
			if r!=-1 and array[l]<array[r]:
				largest=r
			else:
				largest=l
			if array[largest]>array[i]:
				array[i],array[largest]=array[largest],array[i]
				i=largest
				l=2*i+1
			else:
				return
	
	lastnonleafparent=len(array)//2-1
	for i in reversed(range(lastnonleafparent+1)):
		heapify(array,i,len(array)-1)
	
	# keep deleting root
	for i in reversed(range(len(array))):
		print(i)
		array[0],array[i]=array[i],array[0] # root moved to last
		heapify(array,0,i-1)
	
	return array
		
    pass
