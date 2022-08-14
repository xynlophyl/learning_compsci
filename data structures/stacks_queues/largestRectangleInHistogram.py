def largestRectangleArea(heights):
  '''
  goal: find the largest area covered by a subsection of the histogram given by heights
  heights: list[int]
  return: int
  '''
  
  stack = []
  max_area = 0
  for i, h in enumerate(heights):
    start = i 
    if stack:
      while stack and stack[-1][1] > h:
        j, prev = stack.pop()
        max_area = max(max_area, prev*(i-j))
        start = j
    stack.append((start,h))
  
  while stack:
    i, h = stack.pop()
    max_area = max((len(heights)-i)*h, max_area)
  return max_area
