def wordBreak(s, wordDict):
  '''
  goal: given a string, s, and an array of strings, wordDict, check whether s can be completed using strings from wordDict
  s: str, wordDict: list[str]
  return: bool
  '''
  opt = [False] * (len(s)+1)
  opt[len(s)] = True
  
  for i in range(len(s)-1, -1, -1):
    for w in wordDict:
      if (i+len(w)) <= len(s) and s[i:i+len(w)] == w:
        opt[i] = opt[i+len(w)]
      if opt[i]:
        break
        
  return opt[0]
