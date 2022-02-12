def threeNumberSum(array, targetSum):
    res=[]
	def si(L, obj):
		try:
			return L.index(obj)
		except ValueError:
			return -1
	array.sort()
	n=len(array)
	for i in range(n-2):
		l=i+1
		r=n-1
		while(l<r):
			if array[i]+array[l]+array[r]==targetSum:
				res.append([array[i],array[l],array[r]])
				l+=1
				r-=1
			elif array[i]+array[l]+array[r]<targetSum:
				l+=1
			else:
				r-=1
	return res
    pass
