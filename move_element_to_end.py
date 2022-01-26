def moveElementToEnd(array, toMove):
    end=len(array)-1
	start=0
	while(start<end):
		if(array[start]==toMove):
			if(array[end]==toMove):
				end-=1
			else:
				array[start],array[end]=array[end],array[start]
				end-=1
				start+=1
		else:
			start+=1
	return array
    pass
