def palindromePartitioningMinCuts(string):
    def ispalindrome(string):
		l=0
		r=len(string)-1
		while(l<r):
			if string[l]!=string[r]:
				return False
			l+=1
			r-=1
		return True
    pal=[[False for i in range(len(string))] for j in range(len(string))]
	for i in range(len(string)):
		for j in range(len(string)):
			pal[i][j]=ispalindrome(string[i:j+1])
	
	cuts=[float('inf') for i in range(len(string))]
	for i in range(len(string)):
		if pal[0][i]:
			cuts[i]=0
		else:
			cuts[i]=cuts[i-1]+1
			for j in range(1,i):
				if pal[j][i] and cuts[j-1]+1<cuts[i]:
					cuts[i]=cuts[j-1]+1
	return cuts[-1]
    pass
