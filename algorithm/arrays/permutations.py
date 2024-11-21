def permute(nums):
  '''
  goal: return all permutations of nums
  nums: list[int]
  return: list[list[int]]
  '''
  ret = []
  if len(nums) == 1:
    return [nums]
  for i, val in enumerate(nums):
    for perm in permute(nums[:i]+nums[i+1:]):
      ret.append([val]+perm)
  return ret
