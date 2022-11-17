#Input: Two non negative integrs
#Output: Summation of two  number 



#Additon of two numbers how you normally go about basic addition but we implement the use of linkedList data structures


def addTwoNumber(self,value1:Optional[ListNode],value2:Optinoal[ListNode])->: Optional[ListNode]:




	overhead = 0
	sum_1 = ListNode()
	summation = sum_1
	#we use or because can handle 0 values in our addition 
	while value1 or value2 or overhead:
		a = value1.val if value1 else 0#creating a variable to store values in the linkedlist 
		b = value2.val if value2 else 0#Linked list values or data are stoered in the node-> data

		sum_fr = a + b + overhead
		sum_fr = sum_fr % 10
		overhead = sum_fr //10

		summation = ListNode(sum_fr)#adding a node to the linkedlist
		summation = summation.next # moving to the poition in the linked list


		value1=value1.next if value1 else None
		value2=value2.next if value2 else None


	return sum_1.next
