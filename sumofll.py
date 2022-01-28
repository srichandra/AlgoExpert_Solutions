# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(node1, node2):
	head=None
	result=head
	carry=0
	while((node1) and (node2)):
		val_sum=(node1.value+node2.value+carry)%10
		carry=(node1.value+node2.value+carry)//10
		new=LinkedList(val_sum)
		if (head is None):
			head=new
			result=new
			node1=node1.next
			node2=node2.next
		else:
			result.next=new
			node1=node1.next
			node2=node2.next
			result=result.next
		
	# comes out when one of them is none
	while(node1):
		new=LinkedList((node1.value+carry)%10)
		carry=(node1.value+carry)//10
		if (head is None):
			head=new
			result=new
			node1=node1.next
		else:
			result.next=new
			node1=node1.next
			result=result.next
	while(node2):
		new=LinkedList((node2.value+carry)%10)
		carry=(node2.value+carry)//10
		if (head is None):
			head=new
			result=new
			node2=node2.next
		else:
			result.next=new
			node2=node2.next
			result=result.next	
	if(carry):
		new=LinkedList(carry)
		result.next=new
    return head
