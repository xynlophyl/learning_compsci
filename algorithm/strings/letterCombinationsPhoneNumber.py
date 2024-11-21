def letterCombinations(digits):
  '''
  goal: find all the possible letter combinations that a phone number could be mapped to
  digits: str
  return: list[str]

  '''
  if not digits: return []
  m = {
    '2':'abc', '3': 'def', 
    '4': 'ghi', '5':'jkl','6':'mno',
    '7':'pqrs', '8':'tuv', '9':'wxyz'} # map from digits to letter
  
  # solution 2: O(n^2) time, O(1) space
  ret = []
  def backtrack(idx, s):
    if len(s) == len(digits):
      ret.append(s)
      return
    for c in m[digits[idx]]:
      backtrack(idx+1, s+c)
  backtrack(0, '')
  return ret
  
  # solution 1: O(n^2) time, O(n) space
  ret = []
  if len(digits) == 1:
    return m[digits[0]]
  
  for i in m[digits[0]]:
    for j in self.letterCombinations(digits[1:]):
      ret.append(i+j)
      
  return ret
