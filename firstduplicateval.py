def firstDuplicateValue(array):
    for each in array:
		each=abs(each)
		if(array[each-1]<0):
			return each
		else:
			array[each-1]=-1*array[each-1]
    return -1
