def pacificAtlantic(heights):
  '''
  goal: return all cells where water can flow downwards to both oceans (pacific: top and left edges, atlantic: bottom and right edges)
  heights: list[list[int]]
  return: list[list[int]]
  '''

  m,n = len(heights), len(heights[0])
  p,a = set(), set()
  dx, dy = [1,0,-1,0], [0,1,0,-1]
  
  def dfs(r,c, visited, prevHeight):
    if (r,c) in visited or heights[r][c] < prevHeight:
      return
    visited.add((r,c))
    for d in range(4):
      if r+dx[d] >= 0 and r+dx[d] <m and c+dy[d] >=0 and c+dy[d] < n:
        dfs(r+dx[d],c+dy[d], visited, heights[r][c])
  
  for r in range(m):
    dfs(r,0 , p, heights[r][0])
    dfs(r,n-1, a, heights[r][n-1])
    
  for c in range(n) :
    dfs(0,c, p, heights[0][c])
    dfs(m-1,c, a, heights[m-1][c])
  
  ret = []
  for r in range(m):
    for c in range(n):
      if (r,c) in p and (r,c) in a:
        ret.append((r,c))
  return ret