def setZeroes(matrix):
  # multiple passes, more efficient: O(mn) time, O(1) space
  first_col_flag = False
  for r in range(len(matrix)): # finding which cells are 0 -> change the first cell of each row and column to 0 
      if matrix[r][0] == 0:
        first_col_flag = True # extra precaution for top left corner
      for c in range(1, len(matrix[0])): # checking for each cell not in the first row and column
        if matrix[r][c] == 0:
          matrix[r][0] = 0
          matrix[0][c] = 0
  
  for r in range(1,len(matrix)): # changing cells not in first row and column
      for c in range(1,len(matrix[0])):
        if matrix[r][0] == 0 or matrix[0][c] == 0:
          matrix[r][c] = 0
  if matrix[0][0] == 0: #changing cells in the first row
      for c in range(len(matrix[0])):
        matrix[0][c] = 0
  
  if first_col_flag: #changing chells in the first column
      for r in range(len(matrix)):
        matrix[r][0] = 0
  return matrix
  
  # using memory, multiple passes: O(nm) time O(n+m) space
  m = len(matrix)
  n = len(matrix[0])
  rows = set()
  cols = set()
  
  for r in range(len(matrix)):
      for c in range(len(matrix[0])):
        if matrix[r][c] == 0:
          rows.add(r)
          cols.add(c)
  
  for r in range(len(matrix)):
      for c in range(len(matrix[0])):
        if (r in rows or c in cols) and matrix[r][c] != 0:
          matrix[r][c] = 0
  
  return matrix
	