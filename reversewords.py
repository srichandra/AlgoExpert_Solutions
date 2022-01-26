def reverseWordsInString(string):
    # reverse whole string one
	string=[each for each in string]
	reversechars(string,0,len(string)-1)
	start=0
	while(start<len(string)):
		end=start
		while((end<len(string)) and string[end]!=' '):
			end+=1
		reversechars(string,start,end-1)
		start=end+1
	
    return "".join(string)
def reversechars(string,start,end):
	while(start<end):
		string[end],string[start]=string[start],string[end]
		start+=1
		end-=1
