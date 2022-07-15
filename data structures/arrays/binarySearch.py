def search(nums, target):
  '''
  goal: find target's index in nums in logarithmic time
  nums: list[int], target: int
  return: int
  '''
  # recursion implementation
  def binarySearch(nums,target,low,high):
    if low > high:
      return -1
    
    mid = (low+high)//2
    if nums[mid] == target:
      return mid
    elif nums[mid] > target:
      return binarySearch(nums, target, mid+1, high)
    else:
      return binarySearch(nums, target, low, mid-1)
  
  # binary search: O(log n) time, O(1) space
  low, high = 0, len(nums)-1
  
  while low <= high:
    mid = (low+high)//2
    if nums[mid] == target:
      return mid
    elif nums[mid] > target:
      high = mid-1
    else:
      low = mid + 1
  return -1