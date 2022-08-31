def findClosestElements(arr, k, x):
  '''
  goal: find the k closest values to x in arr
  arr: list[int], k: int, x: int
  return: list[int]
  '''
  # binary search
  l, r = 0, len(arr)-k
  
  while l < r:
    m = l + (r-l)//2
    print(arr[m], arr[m+k])
    if x - arr[m] > arr[m+k] - x:
      l = m+1
    else:
      r = m
  return arr[l:l+k]
  
  # heap
  import heapq
  heap = []
  for num in arr:
    heapq.heappush(heap, ((num-x)**2, num))
        
  ret = []
  for i in range(k):
    diff, num = heapq.heappop(heap)
    ret.append(num)
  
  return sorted(ret)
  