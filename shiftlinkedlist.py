# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def shiftLinkedList(head, k):
    # Write your code here.
	start=head
	count=0
	while(start):
		count+=1
		start=start.next
	k=k%count
	if(k==0):
		return head
	# now k is always positive, make kth node from end as head
	first=head
	second=head
	size=count
	count=0
	while(count<k):
		second=second.next
		count+=1
	while(second):
		prev_first=first
		first=first.next
		prev_second=second
		second=second.next
	# now first points to the kth node from end
	prev_second.next=head
	prev_first.next=None
	head=first
	return head
	
		
    pass
