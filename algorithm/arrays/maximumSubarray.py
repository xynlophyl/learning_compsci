def maxSubArray(nums):
  '''
  goal: find the subarray with the max sum in nums and return its sum
  nums: list[int]
  return: int
  '''
  curr_sum = 0
  max_sum = nums[0]
  for i in nums:
    if curr_sum < 0:
      curr_sum = 0
    curr_sum += i
    max_sum = max(max_sum, curr_sum)
    
  return max_sum