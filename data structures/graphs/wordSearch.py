def exist(board, word):
  '''
  goal: return whether you can form word by traversing along board, moving only to adjacent cells horizontally or vertically(can start from any cell)
  board: list[list[str]], word: str
  return: bool
  '''
  # set up
  m,n = len(board), len(board[0])
  used = set()
  
  # defining search function
  def dfs(r,c, idx):    
    if r < 0 or c <0 or r>= m or c >= n or (r,c) in used or board[r][c] != word[idx]:
      return False        
    used.add((r,c))
    if idx + 1 == len(word):
      return True
    res = (dfs(r+1,c,idx+1) or
          dfs(r-1,c,idx+1) or
          dfs(r,c+1,idx+1) or
          dfs(r,c-1,idx+1))
    used.remove((r,c))
    return res
    
  # searching every cell
  for r, row in enumerate(board):
    for c, val in enumerate(row):
      if val == word[0]:
        if dfs(r,c,0):
          return True
  return False

          
              