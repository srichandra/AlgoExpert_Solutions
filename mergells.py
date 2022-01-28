# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(node1, node2):
	head=None
	while(node1 and node2):
		if(node1.value<node2.value):
			if not head:
				head=node1
				curr=head
				node1=node1.next
			else:
				curr.next=node1
				node1=node1.next
				curr=curr.next
		else:
			if not head:
				head=node2
				curr=head
				node2=node2.next
			else:
				curr.next=node2
				node2=node2.next
				curr=curr.next
	while(node1):
		if not head:
			head=node1
			break
		else:
			curr.next=node1
			break
	while(node2):
		if not head:
			head=node2
			break
		else:
			curr.next=node2
			break
	return head
				
    # Write your code here.
    pass
