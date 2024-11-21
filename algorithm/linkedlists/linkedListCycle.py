from ..implementations.linked_lists import ListNode

def hasCycle(head):
  '''
  goal: check whether there is a cycle in the given linked list
  head: ListNode or None
  return: bool
  '''
  # using memory: O(n) time, O(n) space
  if not head:
      return False
  s = set()
  curr = head
  
  while curr.next:
      if curr in s:
          return True
      s.add(curr)
      curr = curr.next
  return False

  # two pointers: O(n) time , O(1) space
  if not head:
      return False
  slow = fast = head
  while True:
      slow = slow.next
      if fast.next and fast.next.next:
          fast = fast.next.next
      else:
          return False
      if slow == fast:
          return True
  