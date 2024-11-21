from ..implementations.linked_lists import ListNode

def reverseList(head):
	'''
	goal: reverse the given linked list return the new head
	head: ListNode or None
	return: ListNode or None
	'''
	# recursion: O(n) time, O(n) space
	if not head:
		return None
	
	newHead = head
	if head.next:
		newHead = reverseList(head.next)
		head.next.next = head
	head.next = None
	return newHead
	
	# iteration: O(n) time, O(1) space
	if not head:
		return None
	
	last = None
	curr = head
	
	while curr:
		# last, curr.next, curr = curr, last, curr.next
		nxt = curr.next
		last, curr.next = curr, last
		curr = nxt
		
	return last
