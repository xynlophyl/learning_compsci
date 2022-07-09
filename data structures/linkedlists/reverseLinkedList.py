def reverseList(head):
	'''
	goal: reverse a linked list
	head: linkedListNode
	return: linkedListNode
	'''
	if not head:
		return None

	prev = next = None
	curr = head

	while curr:
		next = curr.next
		curr.next = prev
		prev = curr
		curr = next
	return prev
	