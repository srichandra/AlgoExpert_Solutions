def topoutil(s,v,adj,st):
		v[s-1]=True
		for each in adj[s]:
			if not v[each-1]:
				topoutil(each,v,adj,st)
		st.append(s)
		return

def topologicalSort(jobs, deps):
	from collections import defaultdict
    adj=defaultdict(list)
	for each in deps:
		adj[each[0]].append(each[1])	
	st=[]
	v=[False for i in range(len(jobs))]
	for each in jobs:
		if not v[each-1]:
			topoutil(each,v,adj,st)
	return st[::-1]
    pass
