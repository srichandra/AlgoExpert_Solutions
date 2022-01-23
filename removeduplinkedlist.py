# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def removeDuplicatesFromLinkedList(linkedList):
    head=linkedList
	prev=head
	curr=head.next
	while(curr):
		if(curr.value==prev.value):
			curr=curr.next
		else:
			prev.next=curr
			prev=curr
			curr=curr.next
	prev.next=curr
    return head
