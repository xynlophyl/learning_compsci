def kClosest(points,  k):
  '''
  goal: find the k closest points to the origin
  points: list[[int,int]], k: int
  return: list[[int,int]]
  '''
  if len(points) == k:
    return points

  # quick select
  curr = [(x**2+y**2, x,y) for x,y in points]
  
  ret = []
  while k != 0:
    pivot = curr[-1][0]
    lt, geq = [], [curr[-1]]
    for i in curr[:-1]:
      if i[0] < pivot:
        lt.append(i)
      else:
        geq.append(i)
    
    if len(lt) <= k:
      ret += lt
      k -= len(lt)
      curr = geq
    else:
      curr = lt
      
  return [(x,y) for dist, x, y in ret]
  
  # heap
  import heapq 
  heap = []
  
  for x,y in points:
    d = -(x**2+y**2)
    if len(heap) == k:
      heapq.heappushpop(heap, (d,x,y))
    else:
      heapq.heappush(heap, (d,x,y))
      
  return [(x,y) for (d,x,y) in heap]
  