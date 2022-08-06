from linked_lists import ListNode
def middleNode(head):
  '''
  goal: find the (rightmost) middle value of the linked list
  head: ListNode or None
  return: ListNode or None
  '''
  # two pointers: O(n) time, O(1) space
  if not head:
    return None
  
  slow = fast = head
  
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
  
  return slow
  