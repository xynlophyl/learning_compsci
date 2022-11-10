def minimumTotal(triangle):
  '''
  goal: given an array, triangle, return the min cost to get to the bottom
  triangle: list[list[int]]
  returns: int
  '''
  def calc(d, row):
    curr = triangle[d]
    if row:
      for i in range(len(curr)):
        curr[i] += row[i]
    
    if d == 0:
      return curr[0]
    
    row = []
    for i in range(len(curr)-1):
      val = min(curr[i], curr[i+1])
      row.append(val)
    
    return calc(d-1, row)
  
  return calc(len(triangle)-1, [])