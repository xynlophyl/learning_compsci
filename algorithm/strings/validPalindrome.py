def isPalindrome(s):
  '''
  goal: check if s is a palindrome (reads same way forward as backwards)
  s: str
  return: bool
  '''
  # constant space two pointers: O(n) time, O(1) space
  low, high = 0, len(s)-1
  
  while low < high:
    if not s[low].isalnum():
      low += 1
    elif not s[high].isalnum():
      high -= 1
    else:
      if s[low].lower() != s[high].lower():
        return False
      low += 1
      high -= 1
  return True
  
  # two pointers with stripping: O(n) time, O(n) space
  new_s = ''
  for i in s:
    if i.isalnum():
      new_s += i.lower()

  low = 0
  high = len(new_s)-1
  while low < high:
    if new_s[low] != new_s[high]:
      return False
    low += 1
    high -= 1
  return True
