def dijkstrasAlgorithm(start, edges):
	def choosemin(D,S):
		mini=float('inf')
		vertex=-1
		for each in range(len(D)):
			if each in S:
				continue
			else:
				if D[each]<mini:
					mini=D[each]
					vertex=each
		return vertex
			
    S=[start]
	n=len(edges)
	D=[float('inf') for i in range(n)]
	for each in edges[start]:
		D[each[0]]=each[1]
	for i in range(1,n):
		w=choosemin(D,S)
		if D[w]==float('inf'):
			break
		S.append(w)
		for edge in edges[w]:
			dest,dist2dest=edge
			if dest in S:
				continue
			D[dest]=min(D[dest],D[w]+dist2dest)
	D[start]=0
	for i in range(n):
		if D[i]==float('inf'):
			D[i]=-1
	return D		
    pass
