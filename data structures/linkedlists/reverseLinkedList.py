def reverseList(head):
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
	