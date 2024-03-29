def twoSum(nums, target):
  '''
  goal: find the indices of two values in nums that sum to target
  nums: list[int], target: int
  return: list[int,int]
  '''
  # using hash table: O(n) time, O(n) space
  d = {}
  for i in range(len(nums)):
    if nums[i] in d:
      return [d[nums[i]],i]
    else:
      d[target-nums[i]] = i
      
  # check every permuation: O(n^2) time, O(1) space
  n = len(nums)
  for i in range(n):
    for j in range(i+1,n):
      if nums[i] + nums[j] == target:
      	return [i,j]
        