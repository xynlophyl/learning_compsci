from linked_lists import ListNode

def removeNthFromEnd(head, n):
  '''
  goal: return the linked list with the nth node from the end removed
  head: ListNode or None, n: int
  return: ListNode or None
  '''
  if not head:
    return None
  
  l = r = head
  while n > 0:
    r = r.next
    n -= 1
  
  prev = None
  dummy = ListNode(next=head)
  
  while r:
    prev = l
    l = l.next
    r = r.next

  if prev:
    prev.next = l.next
  else:
    dummy.next = head.next
  return dummy.next
  