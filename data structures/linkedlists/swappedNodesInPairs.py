from linked_lists import ListNode
def swapPairs(head):
  '''
  goal: return the linked list but with every pair of nodes swapped
  head: ListNode or None
  return: ListNode or None
  '''
  if not head:
    return None
  
  # recursive
  curr = head
  nxt = curr.next
  if nxt:
    next_pair = swapPairs(curr.next.next)
    curr.next.next = curr
    curr.next = next_pair
    return nxt
  return curr
  
  # iterative
  dummy = ListNode(0, head)
  prev = dummy
  curr = head
  
  while curr and curr.next:
    nxt = curr.next
    tmp = nxt.next

    prev.next, nxt.next, curr.next = nxt, curr, tmp
    prev = curr
    curr = tmp

  return dummy.next
  