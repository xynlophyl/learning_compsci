def longestPalindrome(s):
  '''
  goal: find the length of the longest palindrome that can be formed from characters in s (no repeating)
  s: string
  return: int
  '''
  # dictionary: O(n) time, O(n) space
  d = {}

  for i in s:
    d[i] = 1 + d.get(i,0)

  count = 0
  flag = True
  print(d)
  for i in d:
    if d[i]%2==1:
      count += d[i]-1
      if flag:
        count += 1
        flag = False
    else:
      count += d[i]

  return count
