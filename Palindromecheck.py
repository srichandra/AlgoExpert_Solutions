def isPalindrome(string):
	# O(n) time and O(1) space
    left=0
	right=len(string)-1
	valid=True
	while((left<right)&valid):
		if(string[left]==string[right]):
			left+=1
			right-=1
		else:
			valid=False
	return valid
    pass
