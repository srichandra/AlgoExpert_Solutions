def minimumWaitingTime(queries):
    # Write your code here.
	queries.sort()
	tot=0
	for i,each in enumerate(queries):
		tot+=(len(queries)-1-i)*each
    return tot
