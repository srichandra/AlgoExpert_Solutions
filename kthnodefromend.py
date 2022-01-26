# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
	if head is None or head.next is None:
		return head
    p=head
	q=head
	count=1
	while(count<=k):
		q=q.next
		count+=1
	if q is None:
		head.value=head.next.value
		head.next=head.next.next
		return head
	while(q.next):
		p=p.next
		q=q.next
	p.next=p.next.next
	del p
	return head
    pass
