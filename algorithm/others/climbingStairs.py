def climbStairs(n):
  '''
  goal: find the number of ways to climb up to n steps, you can move only one or two steps at a time
  n: int
  return: int
  '''
  steps = {1: 1, 2: 2}
  if n < 3:
    return n
  
  for i in range(3,n):
    steps[i] = steps[i-1] + steps[i-2]
    
  return steps[n-1] + steps[n-2]
    