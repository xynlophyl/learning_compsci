
def isValid(self, s: str) -> bool:
  '''
  goal: check if the given string of parentheses are fully closed in the right order
  s: string
  return: bool
  '''
  brackets = {'(':')', '[':']','{':'}'}
  stack = []
  
  for c in s:
    if c in brackets:
      stack.append(brackets[c])
    else:
      if not stack or stack.pop() != c:
        return False
  
  return not stack
  