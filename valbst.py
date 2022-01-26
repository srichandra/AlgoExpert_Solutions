# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    def valnew(tree,min_val,max_val):
		if not tree:
			return True
		if (min_val>tree.value) or (tree.value>=max_val):
			return False
		return (valnew(tree.left,min_val,tree.value) and valnew(tree.right,tree.value,max_val))
	import math
	return valnew(tree,-math.inf,math.inf)
    pass
