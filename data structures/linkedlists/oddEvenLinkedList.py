from linked_lists import ListNode
def oddEvenList(head):
  '''
  goal: return the linked list with all odd indexes before the even indexes (in order)
  head: ListNode or None
  return: ListNode or None
  '''
  if not head:
    return None
  
  odd, even, evenHead = head, head.next, head.next
  
  while even and even.next:
    odd.next = even.next
    odd = odd.next  
    even.next = odd.next
    even = even.next
  
  odd.next = evenHead
  return head
