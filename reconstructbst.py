# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def getpivot(array):
	root=array[0]
	for i in range(1,len(array)):
		if array[i]>=root:
			return i
	return len(array)
def reconstructBstutil(preOrderTraversalValues):
	if len(preOrderTraversalValues)==0:
		return None
	p=getpivot(preOrderTraversalValues)
	tree=BST(preOrderTraversalValues[0])
	tree.left=reconstructBstutil(preOrderTraversalValues[1:p])
	tree.right=reconstructBstutil(preOrderTraversalValues[p:])
	
	return tree
		
def reconstructBst(preOrderTraversalValues):
    return reconstructBstutil(preOrderTraversalValues)
