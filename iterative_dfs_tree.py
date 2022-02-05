# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        lst=[]
		lst.append(self)
		while(lst):
			cur=lst.pop()
			array.append(cur.name)
			for each in cur.children[::-1]:
				lst.append(each)
		return array
        pass
