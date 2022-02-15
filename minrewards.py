def minRewards(scores):
    # Write your code here.
	r=[1 for each in scores]
	changed=True
	while(changed):	
		changed=False
		for i in range(len(scores)-1):
			if scores[i]>scores[i+1]:
				if r[i]<=r[i+1]:
					r[i]+=1
					changed=True
			elif scores[i]<scores[i+1]:
				if r[i]>=r[i+1]:
					r[i+1]+=1
					changed=True
	return sum(r)
    pass
