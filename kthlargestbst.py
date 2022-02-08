# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
class TreeInfo:
	def __init__(self,count,last):
		self.count=count
		self.last=last

def rorder(root,array,k):
	if root is None:
		return
	
	rorder(root.right,array,k)
	if len(array)==k:
		return
	array.append(root.value)
	rorder(root.left,array,k)
	if len(array)==k:
		return
	
def findKthLargestValueInBst(tree, k):
    array=[]
	rorder(tree,array,k)
	return array[-1]
