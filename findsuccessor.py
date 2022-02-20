# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
		
def findSuccessor(tree, node):
    if node.right is not None:
		return getmin(node.right)
	return getrightmostparent(node)

def getmin(curr):
	while curr.left is not None:
		curr=curr.left
	return curr

def getrightmostparent(node):
	curr=node
	if curr.parent is not None and curr.parent.right==curr:
		curr=curr.parent
	return curr.parent

