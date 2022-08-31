def uniquePaths(m, n):
  '''
  goal: find the number of unique paths to travel from the top left corner to the bottom right of a (m x n) matrix (given that you can only move right or down)
  m: int, n: int
  return: int
  '''
  # optimized
  row = [1] * n
  for i in range(m-1):
    newRow = [1]*n
    for j in range(n-2,-1,-1):
      newRow[j] = newRow[j+1] + row[j]
    row = newRow
  return row[0]

  # my solution
  opt = [[0 for i in range(n)] for i in range(m)]
  opt[0][0] = 1
  
  for r in range(m):
    for c in range(n):
      if r+1 < m:
        opt[r+1][c] += opt[r][c]
      if c+1 < n: 
        opt[r][c+1] += opt[r][c]
  return opt[m-1][n-1]
