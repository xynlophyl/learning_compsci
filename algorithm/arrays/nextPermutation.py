def nextPermutation(nums):
  '''
  goal: modify nums in place, such that you return the next lexigraphical permuation of nums
  nums: list[int]
  return: None
  '''

  def find_decreasing_element(nums):
    i = len(nums)-1
    while i > 0:
      if nums[i-1] < nums[i]: 
        return i-1
      i -= 1
    return -1
  
  def find_next_smallest_number(nums, start):
    i = len(nums)-1
    while nums[i] <= nums[start]:
      i -= 1
    return i
  
  def reverse(nums, start):
    end = len(nums) - 1
    while start < end:
      nums[start], nums[end] = nums[end], nums[start]
      start += 1
      end -= 1
    return nums
  
  i = find_decreasing_element(nums)
  if i >= 0:
    j = find_next_smallest_number(nums, i)
    nums[i], nums[j] = nums[j], nums[i]
  reverse(nums, i+1)
