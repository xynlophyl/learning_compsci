def maxProduct(nums):
  '''
  goal: find the maximum product able to be produced by any subarray from nums
  nums: list[int]
  return: int
  '''
  res = max(nums)
  currMax, currMin = 1, 1
  
  
  for i in nums:
    if i == 0:
      currMin, currMax = 1, 1
      continue
    
    curr = (i*currMax, i*currMin, i)
    currMax = max(curr)
    currMin = min(curr)
    
    res = max(res, currMax)

  return res
