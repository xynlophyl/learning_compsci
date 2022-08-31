def canJump(nums):
  '''
  goal: check whether you can get from start to end of nums, where each position nums represents how far you can traverse through the array
  nums: list[int]
  return: bool
  '''
  goal = len(nums)-1
  
  for i in range(len(nums)-1, -1, -1):
    if i + nums[i] >= goal:
      goal = i
      
  return goal == 0
