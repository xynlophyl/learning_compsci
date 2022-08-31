def canPartition(nums):
  '''
  goal: given an array of ints, nums, check whether it can be partition into two subsets that are equal in value
  nums: int
  return: bool
  '''
  if sum(nums)%2:
    return False
  
  target = sum(nums)//2
  s = set()
  
  for i in range(len(nums)-1, -1, -1):
    curr = nums[i]
    next_s = set()
    for j in s:
      next_s.add(curr+j)
      next_s.add(j)
    next_s.add(curr)
    s = next_s

  return target in s   
