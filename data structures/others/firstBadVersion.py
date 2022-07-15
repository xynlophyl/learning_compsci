def firstBadVersion(n):
  '''
  goal: given a number of product versions, find the first faulty/bad version using isBadVersion API
  n: int
  return: int
  '''
  # binary search: O(log n) time, O(1) space
  def firstBadHelper(low, high):
    if low > high:
      return low
    mid = (low+high)//2
    if isBadVersion(mid):
      return firstBadHelper(low, mid-1)
    return firstBadHelper(mid+1, high)
  
  return firstBadHelper(1,n)
