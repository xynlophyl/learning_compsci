def shortest_path(target_map):
  '''
  goal: find the shortest path from the top left of target_map to the cell with value 2
  target_map: list[list[int]]
  return: int
  '''
  # set up
  m, n = len(target_map), len(target_map[0])
  dx, dy = [1,0,-1,0], [0,1,0,-1]
  visited = set()

  # bfs implementation
  queue = [(0,0,0)]

  while queue:
    r,c, distance = queue.pop(0)
    if (r,c) in visited:
      continue
    visited.add((r,c))

    if target_map[r][c] == 2:
      return distance
    elif target_map[r][c] == 0:
      for d in range(4):
        new_r, new_c = r+dx[d], c+ dy[d]
        if (new_r>=0 and new_r<m) and (new_c>=0 and new_c < n):
          queue.append((new_r, new_c, distance+1))
  return -1

  # dfs implementation
  def dfs(r,c, distance):
    min_distance = float('inf')
    if (r,c) in visited:
      return -1
    visited.add((r,c))
    if target_map[r][c] == 2:
      return distance
    elif target_map[r][c] == 0:
      for d in range(4):
        new_r, new_c = r+dx[d], c+ dy[d]
        if (new_r>=0 and new_r<m) and (new_c>=0 and new_c < n):
          dist = dfs(new_r, new_c, distance+1)
          if dist != -1:
            min_distance = min(min_distance, dist)
    visited.remove((r,c))
    if min_distance == float('inf'):
      return -1
    return min_distance

  return dfs(0,0,0)