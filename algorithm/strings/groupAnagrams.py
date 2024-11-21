def groupAnagrams(strs):
  '''
  goal: group strings that are anagrams of each other
  strs: list[str]
  return: list[list[str]]
  '''
  # filter by count of each letter, O(mn) time [m: number of words, n: length of each word] , O(n) space
  d = {}
  for s in strs:
    count = [0]*26
    for c in s:
      count[ord(c)-ord('a')] += 1
    curr = tuple(count)
    if curr in d:
      d[curr].append(s)
    else:
      d[curr] = [s]
  return d.values()
    
  # sorting, O(n^2logm) time, O(n) space
  d = {}
  
  for s in strs:
    curr = ''.join(sorted(s))
    print(curr)
    if curr in d:
      d[curr].append(s)
    else:
      d[curr] = [s]
  
  ret = []
  for i in d:
    ret.append(d[i])
  return ret
