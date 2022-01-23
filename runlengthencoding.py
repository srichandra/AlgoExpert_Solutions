def runLengthEncoding(string):
    # Write your code here.
	out_string=[]
	count=0
	prev=string[0]
	for each in string:
		if((each!=prev) or (count==9)):
			out_string.append(str(count))
			out_string.append(prev)
			count=0
		count+=1
		prev=each
	out_string.append(str(count))
	out_string.append(prev)
	final_string=''.join(x for x in out_string)
	return(final_string)
    pass
