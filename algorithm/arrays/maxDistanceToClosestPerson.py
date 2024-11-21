def maxDistToClosest(seats):
  '''
  goal: given an array of seats in a row, return the max distance a new passenger can sit away from another passenger (denoted by a 1 in the array)
  seats: list[int]
  returns: int
  '''
  # single pass: O(n) time, O(1) space
  count = 0
  max_diff = -1

  for s in seats:
    if s == 1:
      if max_diff == -1:
        max_diff = count
      else:
        max_diff = max(max_diff, (count+1)//2)
      count = 0
    else:
      count += 1

  if max_diff == -1:
    return count
  else:
    return max(max_diff, count)