def waterArea(heights):
	adj=[0 for i in range(len(heights))]
    for i in range(1,len(heights)-1): # ignore first and last
		l=0
		r=len(heights)-1
		maxl=0
		maxr=0
		while(l<i):
			maxl=max(heights[l],maxl)
			l+=1
		while(r>i):
			maxr=max(heights[r],maxr)
			r-=1		
		adj[i]=min(maxl,maxr)
	sum=0
	for i in range(len(heights)):
		store=max(0,adj[i]-heights[i])	
		sum+=store
	return sum
	
    pass
