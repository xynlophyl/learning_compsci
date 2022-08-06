def wordSubsets(words1, words2):
  '''
  goal: find all the words in words1 that can form the words in words2
  words1: list[str], words2: list[str]
  return: list[str]
  '''
  def count(word):
    # find the count of words
    counts  = [0]*26
    for c in word:
      counts[ord(c)-ord('a')] += 1
    return counts
  
  def subsetCheck(x, y):
    # check if y is a subset of x
    for i in range(26):
      if x[i] < y[i]:
        return False
    return True
  
  # getting the max count of each letter for each word in words2
  max_count = [0]*26
  for word in words2:
    for i, c in enumerate(count(word)):
      max_count[i] = max(max_count[i], c)
  
  # finding words in words1 that have at least the max count 
  ret = []
  for word in words1:
    curr = count(word)
    if subsetCheck(curr, max_count):
      ret.append(word)
  
  return ret
