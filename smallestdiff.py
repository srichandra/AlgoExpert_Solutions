def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
	arrayTwo.sort()
	l1=0
	l2=0
	diffsf=float("inf")
	while(l1<len(arrayOne) and l2<len(arrayTwo)):
		num1=arrayOne[l1]
		num2=arrayTwo[l2]
		diff=abs(num1-num2)
		if diff==0:
			return [num1,num2]
		elif num1<num2:
			l1+=1
		else:
			l2+=1
		if diff<diffsf:
			diffsf=diff
			p=[num1,num2]
	return p	
    pass
