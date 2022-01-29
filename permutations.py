def getPermutations(array):
    perms=[]
	util(0,array,perms)
	return perms
def util(i,array,perms):
	if i==len(array)-1:
		perms.append(array[:])
	else:
		for j in range(i,len(array)):
			swap(array,i,j)			
			util(i+1,array,perms)
			swap(array,i,j)
def swap(array,i,j):
	array[i],array[j]=array[j],array[i]
