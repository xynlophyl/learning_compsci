def champagneTower(poured, query_row, query_glass):
  '''
  setup: there is a pyramid of glasses with 100 rows. Each glass is initially empty, but can take 1 unit of champange, before it overflows to its supporting glasses below (in a 1:1 ratio)
  goal: given the number of units poured into the top glass, return the volume remaining in the query(th)_glass from the query(th)_row
  poured: int, query_row: int, query_glass: int
  '''
  def pour(overflow, d):
    if d == query_row:
      if overflow[query_glass] > 1:
        return 1
      else:
        return overflow[query_glass]
    next_row = [0] * (d+2)
    for i in range(d+1):
      if overflow[i] > 1:
        next_row[i] += (overflow[i]-1)/2
        next_row[i+1] += (overflow[i]-1)/2
    
    return pour(next_row, d+1)
  
  return pour([poured], 0)