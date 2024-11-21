import heapq
def topKFrequent(words, k):
  '''
  goal: find the k most frequent words in words (if two words have the same frequency, sort by lexicographical order)
  words: list[str], k: int
  return list[str]
  '''
  counts = {}
  heap = []
  
  for word in words:
    counts[word] = counts.get(word, 0) + 1
    
  for word in counts:
    heapq.heappush(heap, (-counts[word], word))
    
  ret = []
  while k:
    count, word = heapq.heappop(heap)
    ret.append(word)
    k -= 1
  return ret
      