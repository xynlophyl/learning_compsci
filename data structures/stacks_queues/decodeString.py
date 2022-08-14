def decodeString(s):
  '''
  goal: decode the string, where each substring is multiplied by the number surrounding it
  s: string
  return: string
  '''
  
  # stack
  nums = []
  subs = []
  sub = ''
  m = ''
  
  for curr in s:
    if curr == ']':
      mult = nums.pop()
      sub = subs.pop() + sub*mult
    elif curr == '[':
      nums.append(int(m))
      subs.append(sub)
      m, sub = '', ''
    elif curr.isnumeric():
      m += curr
    else:
      sub += curr
      
  return sub
  
  # recursive
  def helper(s, idx):
    mult = ''
    sub = ''
    while idx < len(s):
      curr = s[idx]
      if curr == "]":
        return sub, idx
      elif curr == "[":
        x = helper(s, idx+1)
        sub += x[0]*int(mult)
        mult = ''
        idx = x[1]
      elif curr.isnumeric():
        mult += curr
      else:
        sub += curr
      idx += 1
    return sub, idx
  return helper(s, 0)[0]
