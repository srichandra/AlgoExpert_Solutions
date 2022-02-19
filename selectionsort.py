def selectionSort(array):
    curr=0
	while(curr<len(array)-1):
		minid=curr
		for i in range(curr+1,len(array)):
			if array[i]<array[minid]:
				minid=i
		array[curr],array[minid]=array[minid],array[curr]
		curr+=1
	return array
    pass
