def maxSubsetSumNoAdjacent(array):
	if len(array)==0:
		return 0
	if len(array)==1:
		return array[0]
    S=[each for each in array]
	S[1]=max(S[0],S[1])
	for i in range(2,len(array)):
		S[i]=max(S[i-1],S[i]+S[i-2])
	maxi=0
	for i in range(len(S)):
		maxi=max(maxi,S[i])
	return maxi
    pass
