def nodeDepths(root):
    # Write your code here.
	def computenew(node,depth):
		if(node==None):
			return 0
		else:
			return depth+computenew(node.left,depth+1)+computenew(node.right,depth+1)
			
    return(computenew(root,0))
	pass


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
