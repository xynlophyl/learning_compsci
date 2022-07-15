def updateMatrix(mat):
  '''
  goal: find the closest distance to a 0 at each cell
  mat: list[list[int]]
  returns: list[list[int]]
  '''
  m,n = len(mat), len(mat[0])

  # bfs: O(mn) time, O(1) space
  queue = []
  ans = [[float('inf') for i in range(n)] for j in range(m)]
  for r, row in enumerate(mat):
    for c, val in enumerate(row):
      if val == 0:
        queue.append((r,c))
        ans[r][c] = 0
    
  while queue:
    r,c = queue.pop(0)
    if r-1 >= 0 and ans[r-1][c] > ans[r][c] + 1:
      ans[r-1][c] = ans[r][c]+1
      queue.append((r-1,c))
    if r+1 < m and ans[r+1][c] > ans[r][c] + 1:
      ans[r+1][c] = ans[r][c]+1
      queue.append((r+1,c))
    if c-1 >= 0 and ans[r][c-1] > ans[r][c] + 1:
      ans[r][c-1] = ans[r][c]+1
      queue.append((r,c-1))
    if c+1 < n and ans[r][c+1] > ans[r][c] + 1:
      ans[r][c+1] = ans[r][c]+1
      queue.append((r,c+1))
  return ans
  # dynamic programming: O(mn) time, O(1) space
  
  if not mat:
    return mat
  
  ans = [[float('inf') for i in range(n)] for j in range(m)]
  for r, row in enumerate(mat):
    for c, val in enumerate(row):
      if val == 0:
        ans[r][c] = 0
      else:
        if r > 0:
          ans[r][c] = min(ans[r-1][c]+1, ans[r][c])
        if c > 0:
          ans[r][c] = min(ans[r][c-1]+1, ans[r][c])
  for r in range(m-1, -1, -1):
    for c in range(n-1, -1, -1):
      if (r < m-1):
        ans[r][c] = min(ans[r+1][c]+1,ans[r][c])
      if (c < n-1):
        ans[r][c] = min(ans[r][c+1]+1, ans[r][c])
  return ans
      