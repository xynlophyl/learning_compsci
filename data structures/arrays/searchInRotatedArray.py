def search(nums, target):
  '''
  goal: given a sorted array that has been rotated by a certain degree, find target's index
  nums: list[int], target: int
  return: int
  '''
  # O(log n) time, O(1) space
  low, high = 0, len(nums)-1
  
  while low<=high:
    mid = low + (high-low)//2
    # print(mid, nums[mid])
    if nums[mid] == target:
      return mid
    
    if nums[low] <= nums[mid]:
      if target > nums[mid] or target < nums[low]:
        low = mid + 1
      else:
        high = mid - 1
    else:
      if target < nums[mid] or target > nums[high]:
        high = mid - 1
      else:
        low = mid + 1
  return -1
  
  # find rotation factor, then binary search: O(n) time, O(1) space
  i = 1
  while i < len(nums): # find rotation O(n) time
    if nums[i] < nums[i-1]:
      break
    i += 1
  
  low, high = 0, len(nums)-1 # binary search O(log n) time
  newNums = nums[i:] + nums[:i]
  while low <= high:
    mid = (low+high)//2
    if newNums[mid] == target:
      return (mid+i)%len(nums)
    elif newNums[mid] > target:
      high = mid - 1
    else:
      low = mid +1
  return -1