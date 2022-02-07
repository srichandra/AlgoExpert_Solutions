def issafe(i,j,vis,matrix):
	return (0<=i<len(matrix) and 0<=j<len(matrix[0]) and matrix[i][j]==1 and vis[i][j]==0)
def DFS(i,j,vis,matrix):
	r = [-1,0,0, 1]
    c = [0,-1,1, 0]
	vis[i][j]=1
	matrix[i][j]=2
	for k in range(4):
		if issafe(i+r[k],j+c[k],vis,matrix):
			DFS(i+r[k],j+c[k],vis,matrix)
	return
def removeIslands(matrix):
	count=0
	m=len(matrix)
	n=len(matrix[0])
	vis = [[0 for i in range(n)] for j in range(m)]
	for i in range(m):
		for j in range(n):
			if((i==0 or i==m-1) or (j==0 or j==n-1)):
				if issafe(i,j,vis,matrix):
                	DFS(i, j,vis,matrix)
	
	for i in range(m):
		for j in range(n):
			if matrix[i][j]==1:
				matrix[i][j]=0
			if matrix[i][j]==2:
				matrix[i][j]=1
	return matrix	
    pass
