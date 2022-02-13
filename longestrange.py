def largestRange(array):
    # Write your code here.
	best=[]
	longl=0
	nums={}
	for num in array:
		nums[num]= True
	for num in array:
		if not nums[num]:
			continue
		nums[num]=False
		curr=1
		left=num-1
		right=num+1
		while left in nums:
			nums[left]=False
			curr+=1
			left-=1
		while right in nums:
			nums[right]=False
			curr+=1
			right+=1
		if curr>longl:
			longl=curr
			best=[left+1,right-1]
	return best
			
