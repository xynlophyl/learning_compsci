def findMaxLength(nums):
  '''
  goal find the longest length of nums where the number of 1 and 0 is the same
  nums: list[int]
  return: int
  '''
  # hash map, keep track of first instance of counter: O(n) time, O(n) space
  d = {0:-1}
  count = 0
  max_length = 0
  
  for i, num in enumerate(nums):
    if num == 0:
      count -= 1
    else:
      count += 1
    
    if count in d:
      max_length = max(max_length, i-d[count])
    else:
      d[count] = i
          
  return max_length