def productSum(array):
    def productSumnew(array,mult):
		sum=0
		for each in array:
			if(type(each)==int):
				sum+=each
			else:
				sum=sum+productSumnew(each,mult+1)
		return sum*mult
	return productSumnew(array,1)
    pass
