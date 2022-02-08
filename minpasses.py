def minimumPassesOfMatrix(matrix):
	n_pass=getpass(matrix)
	return n_pass-1 if not hasneg(matrix) else -1
	
def getadjacent(i,j,matrix):
	adj=[]
	if (i>0):
		adj.append([i-1,j])
	if(i<len(matrix)-1):
		adj.append([i+1,j])
	if (j>0):
		adj.append([i,j-1])
	if(j<len(matrix[0])-1):
		adj.append([i,j+1])
	return adj
def getpos(matrix):
	queue=[]
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if matrix[i][j]>0:
				queue.append([i,j])
	return queue
def getpass(matrix):
	queue=getpos(matrix)
	n_pass=0
	while(len(queue)>0):
		currsize=len(queue)
		while(currsize>0):
			curr=queue.pop(0)
			adj=getadjacent(curr[0],curr[1],matrix)
			for each in adj:
				r,c=each[0],each[1]
				if(matrix[r][c]<0):
					matrix[r][c]*=-1
					queue.append([r,c])
			currsize-=1
		n_pass+=1
		
	return n_pass


def hasneg(matrix):
	for row in matrix:
		for val in row:
			if val<0:
				return True
	return False

