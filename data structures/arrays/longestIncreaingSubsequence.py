def lengthOfLIS(nums):
  '''
  goal: find the length of the longest increasing subsequence of nums that is strictly increasing
  nums: list[int]
  return: int
  '''
  
  opt = [1 for i in nums]
  
  for i in range(len(nums)-1, -1, -1):
    for j in range(i+1, len(nums)):
      if nums[i] < nums[j]:
        opt[i] = max(opt[i], 1+opt[j])
  
  return max(opt)
