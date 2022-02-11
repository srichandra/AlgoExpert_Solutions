def isvalid(o,c):
	return o[0]<c[0]  and o[1]<c[1] and o[2]<c[2]
def diskStacking(disks):   
	n=len(disks)
	disks.sort(key= lambda x:x[2])
	L=[disks[i][2] for i in range(n)]

	for i in range(1,n):
		for j in range(0,i):
			if isvalid(disks[j],disks[i]):
				if L[i]<L[j]+disks[i][2]:
					L[i]=L[j]+disks[i][2]

	maxi=float('-inf')
	maxind=0
	for i in range(n):
		if L[i]> maxi:
			maxi=L[i]
			maxind=i
	res=[]
	res.append(disks[maxind])
	i=maxind
	j=i-1
	while(j>=0):
		if L[i]==L[j]+disks[i][2]:
			res.append(disks[j])
			i=j
			j=i-1
		else:
			j=j-1
	return res[::-1]
	
	
    pass
