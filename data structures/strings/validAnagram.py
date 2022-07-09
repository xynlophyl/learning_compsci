def isAnagram(s, t):
  '''
  goal: check if s and t are anagrams of each other
  s: str, t: str
  return: bool
  '''
  # sorting: O(nlogn) time O(1) space
  return sorted(s) == sorted(t)

  # using dictionary, multiple passes: O(n) time, O(n) space
  if len(s) != len(t):
    return False

  d = {}
  for i in s:
    if i in d:
      d[i] += 1
    else:
      d[i] = 1

  for i in t:
    if i not in d or d[i] == 0:
      return False
    d[i] -= 1
  return True
