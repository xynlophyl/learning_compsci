def longestCommonPrefix(strs):
  '''
  goal: find the longest common prefix in every string of strs
  strs: list[str]
  return: str
  '''
  if not strs:
    return ''
  # Implementing Trie: O(S) time [O(m) to find LCP after creating trie], O(S) space
  
  
  # divide and conquer: O(mn) time, O(mlog n) space   
  def divideAndConquer(strs,l,r):
    if r-l == 1:
      return strs[l]
    mid = (r+l)//2
    left = divideAndConquer(strs, l, mid)
    right = divideAndConquer(strs, mid, r)
    
    for i in range(min(len(left),len(right))):
      if left[i] != right[i]:
        return left[:i]
    return left[:min(len(left),len(right))]
  
  return divideAndConquer(strs, 0, len(strs))
  
  # check every index of every string: O(mn) time [m: length of strs, n: length of shortest s], O(1) space
  idx = 0
  while True:
    for s in strs:
      if idx == len(s):
        return s
      if s[idx] != strs[0][idx]:
        return s[:idx]
    idx += 1
  
  # binary search: O(mnlogm) time, O(1) space
  def isCommon(strs,mid): # O(n)
    for s in strs[1:]:
      if strs[0][:mid] != s[:mid]:
        return False
    return True 
  
  low, high = 0, float('inf')
  for s in strs: # O(m)
    high = min(len(s),high)
  
  while low <= high: # log(m)
    mid = (low+high)//2
    print(mid)
    if isCommon(strs,mid):
      low = mid+1
    else:
      high = mid-1
  return strs[0][:(low+high)//2]
    