def containsDuplicate(nums):
  # sort, then check adjacent indices: O(nlogn) time, O(1) space
  nums.sort()
  
  for i in range(len(nums)-1):
    if nums[i] == nums[i+1]:
      return True
  return False
  
  # using memory: O(n) time, O(n) space
  s = set()
  for i in nums:
    if i in s:
      return True
    s.add(i)
  return False