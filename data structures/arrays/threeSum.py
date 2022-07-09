def threeSum(nums):
  '''
  goal: find all triples in nums with values that sum to 0
  nums: list[int]
  return: list[list[int]]
  '''
  if len(nums) < 3:
    return []
  # sorting then two sum: O(n^2) time, O(1) space          
  nums.sort() # sorts nums so we can see when to move up or down to list
  ret = []
  for idx, num in enumerate(nums):
    if idx > 0 and num == nums[idx-1]:
      continue
      
    low, high = idx+1, len(nums)-1
    while low < high:
      target = nums[low] + nums[high] + num
      if target == 0:
        ret.append([num,nums[low],nums[high]])
        low += 1
        while low < high and nums[low] == nums[low-1]:
          low += 1
      elif target > 0:
        high -= 1
      else:
        low += 1
      
  return ret
