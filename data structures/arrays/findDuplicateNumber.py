def findDuplicate(nums):
  # floyd's cycle detection algorithm (tortoise and hare): O(n) time, O(1) space 

  slow = fast = nums[0]
  
  while True:
    slow = nums[slow]
    fast = nums[nums[fast]]
    if slow == fast:
      break
  
  slow = nums[0]
  
  while slow != fast:
    slow = nums[slow]
    fast = nums[fast]
  return fast