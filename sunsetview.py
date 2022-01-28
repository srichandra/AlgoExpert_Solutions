def sunsetViews(buildings, direction):
    # Write your code here.
	step=1
	maxh=-1
	result=[]
	if direction=='EAST':
		step=-1
	print(step)
	for i,each in enumerate(buildings[::step]):
		if(each>maxh):
			result.append(i)
		maxh=max(maxh,each)
		print(maxh,result)
	if(step==-1):
		return [len(buildings)-1-x for x in result[::-1]]
	else:
		return result 
