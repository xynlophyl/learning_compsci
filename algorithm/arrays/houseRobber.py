def rob(nums):
  '''
  goal: given that a robber can't rob two adjacent houses, find the maxium value they can rob from a street of houses, nums
  nums: list[int]
  return: int
  '''
  if len(nums) < 2:
    return nums[0]
  
  opt = [-1 for i in nums]
  opt[0] = nums[0]
  opt[1] = max(nums[0], nums[1])
  
  for i in range(2, len(nums)):
    opt[i] = max(opt[i-1], opt[i-2] + nums[i])
    
  return opt[-1]