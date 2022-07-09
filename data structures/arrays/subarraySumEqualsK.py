def subarraySum(nums, k):
  '''
  goal: find the number of subarrays with sum equal to k
  nums: list[int], k: int
  return: int
  '''
  # prefix sum with dictionary: O(n) time, O(n) space
  prefixSum = 0
  d = {0: 1}
  count = 0

  for num in nums:
    prefixSum += num
    if prefixSum-k in d:
      count += d[prefixSum-k]
      
    if prefixSum in d:
      d[prefixSum] += 1
    else:
      d[prefixSum] = 1
      
  return count
