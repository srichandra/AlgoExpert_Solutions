def nonConstructibleChange(coins):
    if(len(coins)==0): return 1
	current =0
	coins.sort()
	for each in coins:
		if(each>current+1):
			return current+1
		else:
			current=current+each
			
    return current+1
