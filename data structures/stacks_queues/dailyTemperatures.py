def dailyTemperatures(temperatures):
  '''
  goal: for each day, find the number of days till a day with a higher temperature
  temperatures: list[int]
  return: list[int]
  '''
  # using stack to store indexes
  ret = [0] * len(temperatures)
  stack = []
  
  for i, temp in enumerate(temperatures):
    if stack:
      while stack and temp > temperatures[stack[-1]]:
        idx = stack.pop()
        ret[idx] =  i-idx
    stack.append(i)
  
  return ret
  