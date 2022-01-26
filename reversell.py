# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
	if((head==None) or head.next==None):
		return head
	else:
		p=head.next
		q=head
		q.next=None
		while(p):				
			n=p.next
			p.next=q
			q=p
			p=n
		return q
    pass
