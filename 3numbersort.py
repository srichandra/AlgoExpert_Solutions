def threeNumberSort(array, order):
    first=0
	last=len(array)-1
	mid=0
	i=0
	
	print(array,order)
	while(mid<=last):	
		if(array[mid]==order[0]):
			array[first],array[mid]=array[mid],array[first]
			first+=1
			mid+=1
		elif(array[mid]==order[1]):			
			mid+=1
		else:
			array[last],array[mid]=array[mid],array[last]
			last-=1
	return array
    pass
