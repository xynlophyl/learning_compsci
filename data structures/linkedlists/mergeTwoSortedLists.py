from linked_lists import ListNode
def mergeTwoLists(list1, list2):
  '''
  goal: merge two sorted linked lists
  list1: ListNode or None, list2: ListNode or None
  return: listNode or None
  '''
  if not list1 and not list2:
    return None
  
  dummy = ListNode()
  curr = dummy
  
  while list1 and list2:
    if list1.val > list2.val:
      curr.next, list2 = list2, list2.next
    else:
      curr.next, list1 = list1, list1.next
    curr = curr.next
    
  if list1:
    curr.next = list1
  if list2:
    curr.next = list2
  return dummy.next
          