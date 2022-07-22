def numIslands(grid):
  '''
  goal: find the number of islands (distinct areas of 1's) in grid
  grid: list[list[int]]
  return: int
  '''
  m,n = len(grid), len(grid[0])
  visited = set()
  
  count = 0
  for r, row in enumerate(grid):
    for c, val in enumerate(row):
      if (r,c) in visited or grid[r][c] == "0":
        continue
      count += 1
      queue = [(r,c)]
      while queue:
        x,y = queue.pop(0)
        if (x,y) in visited or grid[x][y] == "0":
          continue
        visited.add((x,y))

        if x-1 >= 0:
          queue.append((x-1,y))
        if x+1 < m:
          queue.append((x+1,y))
        if y-1 >= 0:
          queue.append((x,y-1))
        if y+1 < n:
          queue.append((x,y+1))
  return count