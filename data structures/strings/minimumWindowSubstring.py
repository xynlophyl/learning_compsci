def minWindow(s,t):
  '''
  goal: find the smallest substring of s, where the characters can also be used to form t
  s: str, t: str
  return: str
  
  '''
  # sliding window: O(s+t) time, O(s+t) space
  if not t or not s:
    return ''
  
  tDict = {}
  for i in t:
    tDict[i] = tDict.get(i,0) + 1

  low = 0
  sDict = {}
  minLength, window = float('inf'), (-1,-1)
  formed = 0
  
  for high, curr in enumerate(s):
    if curr not in tDict:
      continue
    sDict[curr] = sDict.get(curr,0) + 1
    
    if sDict[curr] == tDict[curr]:
      formed += 1
      
      while low <= high and formed == len(tDict):
        if (high-low+1) < minLength:
          minLength, window = (high-low+1), (low,high+1)
        
        if s[low] in sDict:
          sDict[s[low]] -= 1
          if sDict[s[low]] < tDict[s[low]]:
            formed -= 1
        low += 1
  return s[window[0]:window[1]]
      