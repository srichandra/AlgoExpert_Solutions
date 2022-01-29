def powerset(array):
    # Write your code here.
	px=[[]]
	for each in array:
		for i in range(len(px)):
			curr=px[i]
			px.append(curr+[each])
	return px
