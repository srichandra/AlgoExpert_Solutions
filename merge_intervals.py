def mergeOverlappingIntervals(intervals_start):
    # Write your code here.
	intervals=sorted(intervals_start,key=lambda x:x[0])
	res=[]
	curr=intervals[0]
	res.append(curr)
	print(res)
	for each in intervals:
		currend=curr[1]
		nextstart,nextend=each[0],each[1]
		
		if currend>=nextstart:
			curr[1]=max(currend,nextend)
		else:
			curr=each
			res.append(curr)
	print(res)		
    return res
