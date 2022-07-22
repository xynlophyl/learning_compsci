def minMaxGame(nums):
  '''
  goal: follow the algorithm provided
  nums: list int
  return: int

  algorithm:
    while length of nums, n, > 1:
      if index, i, is even and i < n/2: newNums[i] = max(nums[2*i], nums[2*i+1])
      if index, i, is odd and i < n/2: newNums[i] = min(nums[2*i], nums[2*i+1])
      set nums to newNums
      repeat until n = 1
    return val of leftover index in nums
  '''
  # simulation of provided alogrithm: O(log n) time, O(n) space
  while len(nums) != 1:
    n = len(nums)
    newNums = []
    for i in range(n//2):
      if i%2 ==0:
        curr = min(nums[2*i], nums[2*i+1])
      else:
        curr = max(nums[2*i], nums[2*i+1])
      newNums.append(curr)
    nums = newNums
  return nums[0]