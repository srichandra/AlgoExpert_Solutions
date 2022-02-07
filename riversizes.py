def issafe(i,j,matrix):
	return (0<=i<len(matrix) and 0<=j<len(matrix[0]) and matrix[i][j]==1)
def DFS(i,j,matrix,sofar):
	if not issafe(i,j,matrix):
		return sofar
	r = [-1,0,0, 1]
    c = [0,-1,1, 0]
	matrix[i][j]=-1
	for k in range(4):
		if issafe(i+r[k],j+c[k],matrix):
			sofar+=1
			sofar=DFS(i+r[k],j+c[k],matrix,sofar)
	return sofar		
def riverSizes(matrix):
    count=0
	array=[]
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if issafe(i,j,matrix):
                sofar=DFS(i, j,matrix,1)
				array.append(sofar)
                count += 1
	return array		
			
    pass
