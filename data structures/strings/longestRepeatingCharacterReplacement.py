def characterReplacement(s, k):
  '''
  goal: given string s, find the longest substring of the same character, given you can change k characters to another in the substring.
  s: str, k: int
  return: int
  '''
  count = {}
  low = 0
  maxCount = 0
  maxLength = 0
  
  for high in range(len(s)):
    count[s[high]] = count.get(s[high], 0) + 1
    maxCount = max(count[s[high]],maxCount)
    while (high-low+1)-maxCount > k:
      count[s[low]] -= 1
      low += 1
    maxLength = max(maxLength,high-low+1)
  return maxLength
  