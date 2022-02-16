def getzeroloc(board,l):
	for row in range(9):
		for col in range(9):
			if board[row][col]==0:
				l[0]=row
				l[1]=col
				return True
	return False

def inrow(board,row,num):
	for i in range(9):
		if board[row][i]==num:
			return True
	return False
def incol(board,col,num):
	for i in range(9):
		if board[i][col]==num:
			return True
	return False
def inbox(board,row,col,num):
	for i in range(3):
		for j in range(3):
			if board[row+i][col+j]==num:
				return True
	return False


def issafe(board,row,col,num):
	return (not inrow(board,row,num)) and (not incol(board,col,num)) and (not inbox(board,row-row%3,col-col%3,num))
def solveSudokuUtil(board):
	l=[0,0] # where to place next
    if(not getzeroloc(board,l)):
		return True
	r=l[0]
	c=l[1]
	for num in range(1,10):
		if issafe(board,r,c,num):
			board[r][c]=num
			if solveSudokuUtil(board):
				return True
			board[r][c]=0
    return False
def solveSudoku(board):
	if solveSudokuUtil(board):
		return board
	else:
		return []
