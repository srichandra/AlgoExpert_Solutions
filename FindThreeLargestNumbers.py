def findThreeLargestNumbers(array):
	import math
  result = [-math.inf,-math.inf,-math.inf]
	for i in range(len(array)):
		num=array[i]
		if(num<=result[0]):
			continue
		elif(result[0]<num<=result[1]):
			result[0]=num		
		elif(result[1]<num<=result[2]):
			result[0]=result[1]
			result[1]=num			
		else:
			result[0]=result[1]
			result[1]=result[2]
			result[2]=num	
	return(result)
  pass
