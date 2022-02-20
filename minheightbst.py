def minHeightBstutil(array,l,r):
	while(l<=r):
		m=(l+r)//2
		tree=BST(array[m])
		tree.left=minHeightBstutil(array,l,m-1)
		tree.right=minHeightBstutil(array,m+1,r)
		return tree
	
def minHeightBst(array):
	tree=minHeightBstutil(array,0,len(array)-1)
	return tree
    pass


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
