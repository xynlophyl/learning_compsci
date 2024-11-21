def generateParenthesis(n):
  '''
  goal: find all possible combinations of n well formed parentheses
  n: int
  return: list[str]
  '''
  # tracking closure number
  if n == 0:
    return ['']
  ans = []
  for c in range(n):
    for l in generateParenthesis(c):
      for r in generateParenthesis(n-1-c):
        ans.append(f'({l}){r}')
  return ans
  
  # backtracking
  ret = []
  def backtrack(s, l, r):
    if len(s) == 2*n:
      ret.append(''.join(s))

    if l < n:
      s.append('(')
      backtrack(s, l+1,r)
      s.pop()
    if r < l:
      s.append(')')
      backtrack(s, l, r+1)
      s.pop()

  backtrack([], 0, 0)
  return ret
