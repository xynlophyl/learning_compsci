from linked_lists import ListNode
def addTwoNumbers(l1, l2):
  '''
  goal: given two numbers (represented from back to front in the form a linked list) return the sum
  l1: ListNode or None, l2: ListNode or None
  return: ListNode or None
  '''
  if not l1 and not l2:
    return None
  
  dummy = ListNode()
  curr = dummy
  carry = 0
  
  while l1 or l2 or carry:
    v1 = l1.val if l1 else 0
    v2 = l2.val if l2 else 0
    v = v1 + v2 + carry
    
    carry = v//10
    nextNode = ListNode(v%10)
    curr.next = nextNode
    
    curr = curr.next
    l1 = l1.next if l1 else None
    l2 = l2.next if l2 else None
    
  return dummy.next
