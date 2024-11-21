def addBinary(a,b):
  '''
  goal: add the two binary strings together
  a: str, b: str
  return: str
  '''

  p1, p2 = len(a)-1, len(b)-1
  carry = 0
  ret = ''
  
  while p1 >= 0 or p2 >= 0:
    l, r = a[p1] if p1 >= 0 else 0, b[p2] if p2 >= 0 else 0
    curr = int(l) + int(r) + carry
    remainder = curr%2
    carry = curr//2
    
    ret = str(remainder)+ret
    p1 -= 1
    p2 -= 1
  
  
  return str(carry)+ret if carry else ret

    