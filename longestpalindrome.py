def longestPalindromicSubstring(string):
    # Write your code here.
	
	def utilfunc(string,left,right):
		while left>=0 and right<len(string):
			if(string[left]!=string[right]):
				break
			left-=1
			right+=1
		return [left+1,right]		
	
	out=[0,1]
		

	for i in range(1,len(string)):
		odd=utilfunc(string,i-1,i+1)
		even=utilfunc(string,i-1,i)
		longest=max(odd,even,key=lambda x: x[1]-x[0])
		out=max(longest,out,key=lambda x: x[1]-x[0])
		
	return string[out[0]:out[1]]
