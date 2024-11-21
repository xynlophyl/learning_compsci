import heapq

def leastInterval(tasks, n):
  '''
  goal: given an array of tasks (that can be repeated), and a cooldown, n, between operating the same task, find the time it takes to complete all tasks
  tasks: list[str], n: int
  return: int
  '''
  counts = {}
  for i in tasks:
    counts[i] = 1 + counts.get(i, 0)
  
  heap = []
  for i in counts:
    heapq.heappush(heap, -counts[i])
    
  queue = []
  time = 0
  while heap or queue:
    if heap:
      curr = heapq.heappop(heap)
      if curr < -1:
        queue.append((curr+1, time+n))

    if queue and queue[0][1] == time:
      heapq.heappush(heap, queue.pop(0)[0])
    
    time += 1
    
  return time
