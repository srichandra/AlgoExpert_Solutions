# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def height(tree):
	if tree is None:
		return 0
	else:
		return (1+max(height(tree.left),height(tree.right)))
def diameter(tree):
	if tree is None:
		return 0
	else:
		lheight=height(tree.left)
		rheight=height(tree.right)
		return max(max(diameter(tree.left),diameter(tree.right)),1+lheight+rheight)
		

def binaryTreeDiameter(tree):
	return diameter(tree)-1
