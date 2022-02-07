def cycleInGraph(edges):
	def util(v,vis,rec,edges):
		vis[v]=1
		rec[v]=1
		for each in edges[v]:
			if vis[each]==0:
				if util(each,vis,rec,edges)==True:
					return True
			elif rec[each]==1:
				return True
		rec[v]=0
		return False
	# build graph matrix
    m=len(edges)
	vis=[0 for i in range(m)]
	rec=[0 for j in range(m)]
	for each in range(m):
		if vis[each]==0:
			if util(each,vis,rec,edges)==True:
				return True
	
    return False
