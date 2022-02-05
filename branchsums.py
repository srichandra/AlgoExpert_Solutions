# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    def util(root,sum_array,sofar):
		if root.left is not None and root.right is not None :
			util(root.left,sum_array,sofar+root.value)
			util(root.right,sum_array,sofar+root.value)
		elif root.left is not None:	
			util(root.left,sum_array,sofar+root.value)
		elif root.right is not None:	
			util(root.right,sum_array,sofar+root.value)
		else:
			sum_array.append(sofar+root.value)
			return
	sum_array=[]
	util(root,sum_array,0)
	return sum_array
    pass
