#Input: A Linked list of  integer numbers 
#output: A reverse linked list



def reverseLinkedList(self,head:Optional[ListNode])->Optional[ListNode]:
	prev = None
	curr = head

#This while loop condition allows us to stay within the linked list and lets  us know
#when we get to the ened because i will be null


#how this works needs a bit more than documentation to explain
#diagram will be best
	while head:
		next = curr.next 
		curr.next = prev
		prev = curr
		curr = next 
	return prev




