def subsets(nums):
  '''
  goal: return the powerset (all possible subsets) of nums
  nums: list[int]
  return: list[list[int]]

  '''
  ret = [[]]
  if len(nums) == 0:
    return ret
  
  for i, val in enumerate(nums):
    subset = subsets(nums[i+1:])
    for s in subset:
      s.append(val)
      ret.append(s)
  return ret
  