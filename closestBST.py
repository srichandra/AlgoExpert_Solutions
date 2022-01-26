def findClosestValueInBst(tree, target):
    def findclose(tree,target,close):
		if(not tree):
			return close
		if(tree.value==target):
			return tree.value
		else:
			if(abs(close-target)>abs(tree.value-target)):
				close=tree.value
			if(target>tree.value):
				return findclose(tree.right,target,close)
			else:
				return findclose(tree.left,target,close)
	import math
	return(findclose(tree,target,math.inf))
			
    pass


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
