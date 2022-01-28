def hasSingleCycle(array):
	vis=0
	idx=0
	vis_array=[0]*len(array)
	while(vis<len(array)):
		if():
			break
		idx=(idx+array[idx])%len(array)
		if(idx<0):
			idx+=len(array)
		if(vis_array[idx]==1):
			return False
		else:
			vis_array[idx]=1
			vis+=1
	return True			
    pass
