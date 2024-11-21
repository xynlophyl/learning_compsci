def trap(height):
  '''
  goal: find the volume of water that is able to be trapped in the structure defined by heights
  heights: list[int]
  return: int
  '''
  n = len(height)
  left = [-1] * n
  right = [-1] * n
  
  r_max = l_max = -float('inf')
  for i in range(n):
    r_max = max(r_max, height[i])
    right[i] = r_max
    
  for i in range(n, 0, -1):
    l_max = max(l_max, height[i-1])
    left[i-1] = l_max

  volume = 0
  for i in range(n):
    volume += min(left[i], right[i]) - height[i]
  return volume
  