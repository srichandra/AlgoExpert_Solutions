def countsort(array,exp):
	output=[0]*len(array)
	count=[0]*10
	for each in array:
		idx=each//exp
		idx=idx%10
		count[idx]+=1
	for i in range(1,10):
		count[i]+=count[i-1]
	i=len(array)-1
	while(i>=0):
		idx=array[i]//exp
		idx=idx%10
		outidx=count[idx]
		output[outidx-1]=array[i]
		count[idx]-=1
		i=i-1
	for i in range(len(array)):
		array[i]=output[i]
		
		
def radixSort(array):
	if len(array)==0:
		return array
	exp=1
	max1 = max(array)
	while(max1/exp)>=1:
    	countsort(array,exp)
		exp=exp*10
		print(array)
	return array
