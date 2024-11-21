def minKnightMoves(x, y):
  '''
  goal: what is the minimum amount of moves for knight to reach square (x,y) from (0,0)
  x: int, y: int
  return: int
  '''
  queue = [(0,0,0)]
  moves = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]
  visited = set()

  while queue:
    i,j, count = queue.pop(0)
    if (i,j) in visited: 
      continue
    visited.add((i,j))
    if (i,j) == (x,y):
      return count
    for dx, dy in moves:
      queue.append((i+dx, i+dy, count+1))
