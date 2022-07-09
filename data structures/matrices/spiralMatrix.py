def spiralOrder(matrix):
  '''
  goal: return the matrix as a list in a spiral order
  matrix: list[list[int]]
  return: list[int]
  '''

  dx = [0,1,0,-1] # directions
  dy = [1,0,-1,0]
  r, c = len(matrix), len(matrix[0])
  x = y = d = 0
  
  spiral = []
  for i in range(r*c): 
    spiral.append(matrix[x][y]) #adds current cell to spiral
    matrix[x][y] = 0 # marks the current cell
    next_x = x+dx[d] # sets direction for next position in spiral
    next_y = y+dy[d]
    if (next_x >= r or next_x < 0) or (next_y >= c or next_y < 0) or matrix[next_x][next_y] == 0:
      # if next move in spiral goes out of matrix or is a cell that has been marked, pivots direction by 90 deg 
      d = (d+1)%4 #
      next_x = x+dx[d]
      next_y = y+dy[d]
    x = next_x
    y = next_y
  return spiral
      