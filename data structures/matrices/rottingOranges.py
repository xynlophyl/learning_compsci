def orangesRotting(grid):
  '''
  goal: return the time it will take for all 1's to turn into 2, given that at each time step a 1 connected directly to a 2 will 'rot'.
  grid: list[list[int]]
  return: int
  '''
  m,n = len(grid), len(grid[0])
  
  time = [[-1 for i in range(n)] for i in range(m)]
  rottenQ = []
  for r, row in enumerate(grid):
    for c, val in enumerate(row):
      if val == 2:
        rottenQ.append((r,c))
        time[r][c] = 0
      elif val == 1:
        time[r][c] = float('inf')
      
  ans = 0
  while rottenQ:
    # print(rottenQ)
    r,c = rottenQ.pop(0)
    # print(r,c,m,n)
    curr = time[r][c]+1
    if r-1 >= 0 and curr < time[r-1][c]:
      time[r-1][c] = curr
      rottenQ.append((r-1,c))
    if c-1 >=0 and curr < time[r][c-1]:
      time[r][c-1] = curr
      rottenQ.append((r,c-1))
    if r+1 < m and curr < time[r+1][c]:
      time[r+1][c] = curr
      rottenQ.append((r+1,c))
    if c+1 < n and curr < time[r][c+1]:
      time[r][c+1] = curr
      rottenQ.append((r,c+1))
      
  for r, row in enumerate(time):
    for c, val in enumerate(row):
      if val == float('inf'):
        return -1
      ans = max(ans, val)
  return ans
  
  