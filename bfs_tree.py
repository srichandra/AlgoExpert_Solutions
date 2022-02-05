# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        lst=[]
		lst.append(self)
		while(lst):
			cur=lst.pop(0)
			array.append(cur.name)
			for each in cur.children:
				lst.append(each)
		return array
		
        pass
