def myAtoi(s):
  '''
  goal: return the integer, n, found in s (where -2**31 <= n <= 2**31-1 )
  s: string
  return: int
  '''
  # general approach, following instructions: O(n) time, O(1) space
  if not s:
    return 0
  
  def removeWhitespace(s):
    for i in range(len(s)):
      if s[i] != " ":
        return i
    return -1
  
  def checkSign(x):
    if x == "+":
      return 1
    elif x == "-":
      return -1
    else:
      return 0
  
  def getInt(s):
    num = '0'
    for i in s:
      if not i.isnumeric():
        return int(num)
      num += i
    return int(num)
  
  start = removeWhitespace(s)
  if start == -1:
    return 0
  
  sign = checkSign(s[start])
  if sign != 0:
    start += 1
  else:
    sign = 1
  num = getInt(s[start:])
  
  print(sign, num)
  if sign == 1:
    return min(sign*num,2**31-1)
  return max(sign*num,sign*2**31)
  
    