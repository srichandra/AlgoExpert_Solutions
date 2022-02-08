# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
	d1=0
	curr=descendantOne
	while(curr):
		curr=curr.ancestor
		d1+=1
	curr=descendantTwo
	d2=0
	while(curr):
		curr=curr.ancestor
		d2+=1
	if(d1>d2):
		diff=d1-d2
		first=descendantOne
		second=descendantTwo		
	else:
		diff=d2-d1
		first=descendantTwo
		second=descendantOne
	count=0
	while(count<diff):
		first=first.ancestor
		count+=1
	while(first!=second):
		first=first.ancestor
		second=second.ancestor
	print(second.name)
	return second
	
    pass
