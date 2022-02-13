def validIPAddresses(string):
	def isvalid(string):
		stringint=int(string)
		if stringint>255:
			return False
		return len(string)==len(str(stringint))

    res=[]
	for i in range(1,min(len(string),4)):
		curr=["","","",""]
		curr[0]=string[:i]
		if not isvalid(curr[0]):
			continue
		for j in range(i+1,i+min(len(string)-i,4)):
			curr[1]=string[i:j]
			if not isvalid(curr[1]):
				continue
			for k in range(j+1,j+min(len(string)-j,4)):
				curr[2]=string[j:k]
				curr[3]=string[k:]
				if isvalid(curr[2]) and isvalid(curr[3]):
					res.append(".".join(curr))
	
	return res
