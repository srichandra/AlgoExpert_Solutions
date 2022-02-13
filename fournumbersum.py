def fourNumberSum(array, targetSum):
    allpair={}
	res=[]
	for i in range(1,len(array)-1):
		for j in range(i+1,len(array)):
			curr=array[i]+array[j]
			if targetSum-curr in allpair:
				for pair in allpair[targetSum-curr]:
					res.append(pair+[array[i],array[j]])
		for k in range(0,i):
			curr=array[k]+array[i]
			if curr not in allpair:
				allpair[curr]=[[array[k],array[i]]]
			else:
				allpair[curr].append([array[k],array[i]])
	return res
    pass
