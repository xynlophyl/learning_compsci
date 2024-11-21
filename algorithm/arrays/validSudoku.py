def isValidSudoku(board):
  '''
  goal: figure out if the current state of a sudoku board is valid
  board: list[list[string]]
  return: bool
  '''
  # O(81) time, O(81) space
  
  columnValid = [set() for i in range(9)]
  boxesValid = [set() for i in range(9)]
  for r in range(9): 
    rowValid = set()
    for c in range(9):
      curr = board[r][c]
      if curr == ".":
        continue
      if curr in rowValid:
        return False
      rowValid.add(board[r][c])
      
      if curr in columnValid[c]:
        return False
      columnValid[c].add(curr)
      
      if curr in boxesValid[r//3*3 + c//3]: 
        # each box is numbered 0 - 8 from top left to bottom right
        # to calculate the number of each box, num = row_num//3*3 + col_num//3
        return False
      boxesValid[r//3*3 + c//3].add(curr)
  return True
      