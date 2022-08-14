from ..linkedlists.linked_lists import ListNode
def mergeKLists(lists):
  '''
  goal: given k sorted liked lists, merge into one whole linked list
  lists: list[ListNode or None]
  return: ListNode or None
  '''
  import heapq
  heap = []
  d = {}
  
  for l in lists:
    while l:
      if l.val in d:
        d[l.val].append(l)
      else:
        d[l.val] = [l]
        heapq.heappush(heap, l.val)
      l = l.next
  
  dummy = ListNode()
  curr = dummy
  while heap:
    val = heapq.heappop(heap)
    for node in d[val]:
      curr.next, node.next = node, None
      curr = curr.next
  
  return dummy.next
