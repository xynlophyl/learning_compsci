def longestConsecutive(nums):  
  '''
  goal: return the length of the longest consecutive sequence in nums (in linear time)
  nums: list[int]
  return: int
  '''
  # using memory: O(n) time, O(n) space
  s = set(nums)
  max_count = 0
  for num in s:
    if num-1 not in s: # num is the smallest number in a potential consecutive seq
      curr = num
      count = 1
  
      while curr+1 in s: 
      # loop will only run for the start of every x where x-1 is not in nums
      # this means that every element is visited at most twice in this entire function
      # O(2n) => O(n)
        curr += 1
        count += 1
      max_count = max(count,max_count)
  return max_count
                      
  
  # sorting: O(nlogn) time, O(1) space
  if not nums:
    return 0
  nums.sort()
  count = 1
  max_count = 1
  for i in range(1,len(nums)):
    if nums[i] - nums[i-1] == 1:
      count += 1
    elif nums[i] != nums[i-1]:
      count = 1
    max_count = max(count,max_count)

  return max_count 
