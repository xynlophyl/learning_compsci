def hammingWeight(n):
  '''
  goal: count the number of 1's in the binary representation of n
  n: int
  return: int
  '''
  idx = 0
  count = 0
  while n:
    n = n & (n-1)
    count += 1
    
  return count