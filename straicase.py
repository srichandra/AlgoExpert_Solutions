def staircaseTraversal(height, maxsteps):
    D=[0 for x in range(height+1)]
	for i in range(1,maxsteps+1):
		D[i]=1
	for i in range(height+1):
		for j in range(1,maxsteps+1):
			if j<i:
				D[i]+=D[i-j]
	return D[-1]
