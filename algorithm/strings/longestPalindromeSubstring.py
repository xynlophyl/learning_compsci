def longestPalindrome(s):
  '''
  goal: find the longest substring of s that is a palindrome
  s: str
  return: str
  '''
  # Manacher's Algorithm: O(n) time, O(1) space 
  # source: https://en.wikipedia.org/wiki/Longest_palindromic_substring#Manacher's_algorithm
  
  # expand from center: O(n^2) time, O(1) space
  def findLargestP(s,low,high):
    while low > - 1 and high < len(s) and s[low] == s[high]:
      low -= 1
      high += 1
    return high - low - 1
  
  low = high = 0
  for i in range(len(s)):
    length = max(findLargestP(s,i,i),findLargestP(s,i,i+1))
    if length > high-low:
      low = i -(length-1)//2
      high = i + length//2
  return s[low:high+1]


      