def sortedSquaredArray(array):
    # Write your code here
    left=0
	right=len(array)-1
	result=[0]*len(array)
	idx=len(array)-1
	while(left<right):
		if(abs(array[left])>abs(array[right])):
			result[idx]=array[left]**2
			left+=1
			idx-=1
		else:
			result[idx]=array[right]**2
			right-=1
			idx-=1
		
	result[idx]=array[left]**2
	return result
