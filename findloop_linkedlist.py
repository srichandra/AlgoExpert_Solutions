# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop(head):
	if (head==None) or (head.next==None):
		return None
    slow=head
	fast=head		
	while(fast and fast.next):
		slow=slow.next
		fast=fast.next.next
		if(slow==fast):
			break
	if(slow!=fast):
		return None
	else:
		slow=head
		while(slow!=fast):
			slow=slow.next
			fast=fast.next
		return slow
	
    pass
