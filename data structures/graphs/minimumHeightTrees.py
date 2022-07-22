def findMinHeightTrees(n, edges):
  '''
  goal: given a list of edges, find the list of root nodes that create the trees with the min height
  n: int, edges: list[list[int]]
  return: list[int]
  '''     
  # base case
  if n <= 2:
    return [i for i in range(n)] 
  # set up adjaceny list
  ret = []
  adj = {i: set() for i in range(n)}
  for i, j in edges:
    adj[i].add(j)
    adj[j].add(i)
  
  '''
  Topoglogical sort
  '''
  
  # find nodes that only have one neighbor (i.e parent node)
  leaves = [i for i in range(n) if len(adj[i]) == 1]
  
  # trimming leaves until centroid(s) are left
  remaining = n
  while remaining > 2:
    remaining -= len(leaves)
    next_leaves = []
    while leaves:
      curr = leaves.pop()
      neighbor = adj[curr].pop()
      adj[neighbor].remove(curr)
      if len(adj[neighbor]) == 1:
        next_leaves.append(neighbor)
        
    leaves = next_leaves
  return leaves
  
  '''
  brute force search
  '''
  min_height = float('inf')
  
  for start in range(n):
    visited = set()
    queue = [(start,0)]
    
    while queue:
      curr, height = queue.pop(0)
      if height > min_height or curr in visited:
        continue
      # print('curr', curr, height)
      visited.add(curr)
      for neighbor in adj[curr]:
        if neighbor not in visited:
          queue.append((neighbor,height+1))
    
    # print(start, height)
    if height == min_height:
      ret.append(start)
    elif height < min_height:
      min_height = height
      ret = [start]
  return ret