def findAnagrams(s, p):
  '''
  goal: find all substrings in s that are anagrams of p
  s,p : int
  return: list[int]
  '''
  # comparing counts of each substring with memory, skipping over substrings that do not have letters in p: O(s) time, O(p) space
  if len(p) > len(s):
    return []
  p_count = {}
  for i in p:
    p_count[i] = p_count.get(i,0) + 1
  
  low = high = 0
  ret = []
  s_count = {}
  while high < len(s):
    while high < len(s) and high-low < len(p):
      if s[high] not in p_count:
        s_count = {}
        low = high+1
      else:
        s_count[s[high]] = s_count.get(s[high],0) + 1
      high += 1  
    
    if s_count == p_count:
      ret.append(low)
      
    if high >= len(s):
      break
    s_count[s[low]] -= 1
    low += 1
  return ret          
  
  # naive approach: O(n^2logn), O(n) space
  low, high = 0, len(p)
  sorted_p = sorted(p)
  ret = []
  while high <= len(s):
    if sorted(s[low:high]) == sorted_p:
      ret.append(low)
    low += 1
    high += 1
  return ret
    