def twoNumberSum(array, targetSum):
  ## O(n) for sorted array else O(nlogn)
  array.sort()
	n=len(array)
	i=0
	j=n-1
	while(i<j):
		sum=array[i]+array[j]
		if(sum<targetSum):
			i+=1
		elif(sum>targetSum):
			j-=1
		else:
			return [array[i],array[j]]
	return []
  pass
