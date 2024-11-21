def ladderLength(beginWord, endWord, wordList):
  '''
  goal: if possible, return the fewest amount of transformations from beginWord to endWord using words from wordList (endWord is in wordList), else 0
  beginWord: str, endWord: str, wordList: list[str]
  return: int
  '''
  if endWord not in wordList:
    return 0
  n = len(beginWord)
  
  # optimized approach: create adjacency list by creating patterns for each word (i.e replacing each character with a wildcard) and connecting words with the same pattern
  def optimizedGetEdges(wordList):
    adj = {}
    for word in wordList:
      for i in range(n):
        pattern = word[:i] + "*" + word[i+1:]
        adj[pattern] = adj.get(pattern, []) + [word]
    return adj
  
  # initial approach: connect words if they differ by one character
  # def differAmount(x,y): 
  #   diff = 0
  #   for i in range(n):
  #     if x[i] != y[i]:
  #       diff += 1
  #   return diff

  # def getEdges(wordList):
  #   adj = {word: [] for word in wordList}
  #   for i, x in enumerate(wordList):
  #     for y in wordList[i:]:
  #       if differAmount(x,y) == 1:
  #         adj[x].append(y)
  #         adj[y].append(x)
  #   return adj
  
  # after setting up graph, perform bfs
  wordList.append(beginWord)
  
  # adj = getEdges(wordList)
  adj = optimizedGetEdges(wordList)

  queue = [(beginWord, 1)]
  visited = set()
  while queue:
    curr, count = queue.pop(0)
    if curr in visited:
      continue         
    visited.add(curr)
    if curr == endWord:
      return count
    
    # for word in adj[curr]:
    #   queue.append((word, count + 1))
    
    for i in range(n):
      pattern = curr[:i] + "*" + curr[i+1:]
      for word in adj[pattern]:
        queue.append((word, count+1))
        
  return 0
    