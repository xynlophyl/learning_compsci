def lengthOfLongestSubstring(s):
  '''
  goal: find the length of the longest substring with no repeating characters
  s: str
  return: int
  '''
  # using set, sliding window: O(n) time, O(n) space
  if not s:
    return 0
  low = high = 0
  mem = set()
  max_count = 0
  while high < len(s):
    if s[high] in mem:
      max_count = max(max_count,high-low)
      while s[low] != s[high]:
        mem.remove(s[low])
        low += 1
      low += 1
    else:
      mem.add(s[high])
    high += 1

  return max(max_count,high-low)