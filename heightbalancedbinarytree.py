# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def height(tree):
	if tree is None:
		return 0
	return 1+max(height(tree.left),height(tree.right))
def heightBalancedBinaryTree(tree):
    if tree is None:
		return True
	l=height(tree.left)
	r=height(tree.right)
	return abs(l-r)<2 and heightBalancedBinaryTree(tree.left) and heightBalancedBinaryTree(tree.right)
