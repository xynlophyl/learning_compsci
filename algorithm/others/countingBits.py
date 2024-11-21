def countBits(n):
  '''
  goal: return the number of 1 bits in every single binary number up to n
  n: int
  return: list[int]
  '''
  opt = [0] * (n+1)
  opt[0] = 0
  offset = 1
  
  for i in range(1,n+1):
    if offset*2 == i:
      offset = i
    opt[i] = 1 + opt[i-offset]
  
  return opt
