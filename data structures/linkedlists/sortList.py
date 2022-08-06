from linked_lists import ListNode
def sortList(head):
  '''
  goal: sort the linked list
  head: ListNode or None
  return: ListNode or None
  '''
  if not head or not head.next:
    return head
  
  # top down merge sort: O(n log n), O(log n) space
  def findMid(node):
    s = f = node
    lastMid = node
    while f and f.next:
      lastMid = s
      s = s.next
      f = f.next.next

    lastMid.next = None # splits the list into 2 halves at midpoint
    return s
  
  def merge(l, r):
    dummy = ListNode()
    curr = dummy
    while l and r:
      if l.val < r.val:
        val = l.val
        l = l.next
      else:
        val = r.val
        r = r.next
      curr.next = ListNode(val)
      curr = curr.next
    while l:
      curr.next = l
      curr = curr.next
      l = l.next
    while r:
      curr.next = r
      curr = curr.next
      r = r.next
    return dummy.next
  
  mid = findMid(head)
  l = sortList(head)
  r = sortList(mid)
  return merge(l, r)
    
  # add to list, sort, then reroute each node, O(n log n) time, O(n) space

  d = {}
  curr = head
  while curr:
    if curr.val in d:
      d[curr.val].append(curr)
    else:
      d[curr.val] = [curr]
    nxt = curr.next
    curr.next = None
    curr = nxt
    
  sorted_vals = sorted([i for i in d])
  
  dummy = ListNode()
  curr = dummy
  
  for i in sorted_vals:
    for node in d[i]:
      curr.next = node
      curr = curr.next
    
  return dummy.next
