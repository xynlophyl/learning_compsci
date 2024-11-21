def floodFill(image, sr, sc, color):
  '''
  goal: replace any cell to color if the cell is connected to and matches the color of the starting cell
  image: list[list[int]], sr: int, sc: int, color:int
  return: list[list[int]]
  '''
  if image[sr][sc] == color:
    return image
  
  # recursion implementation: O(n) time, O(n) space

  m = len(image)
  n = len(image[0])
  sColor = image[sr][sc]
  
  def dfs(r,c):
    if image[r][c] == sColor:
      image[r][c] = color
      if r-1 >= 0:
        dfs(r-1,c)
      if r+1 < m:
        dfs(r+1,c)
      if c-1 >= 0:
        dfs(r,c-1)
      if c+1 < n:
        dfs(r,c+1)
  dfs(sr,sc)
  return image
    
  # dfs using stack: O(n) time, O(n) space
  sColor = image[sr][sc]
  m = len(image)
  n = len(image[0])
  stack = [(sr,sc)]
  while stack:
    r, c = stack.pop()
    # print(sColor, r,c, image[r][c])
    if image[r][c] != sColor:
      continue
    image[r][c] = color
    if r-1 >= 0:
      stack.append((r-1,c))
    if r+1 < m:
      stack.append((r+1,c))
    if c-1 >= 0:
      stack.append((r,c-1))
    if c+1 < n:
      stack.append((r,c+1))
  return image
      
      
    