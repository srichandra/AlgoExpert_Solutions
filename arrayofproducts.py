def arrayOfProducts(array):
	res=[1 for _ in range(len(array))]
	leftp=1
	for i in range(len(array)):
		res[i]=leftp
		leftp*=array[i]
	rightp=1
	for i in reversed(range(len(array))):
		res[i]*=rightp
		rightp*=array[i]
	return res	
    pass
