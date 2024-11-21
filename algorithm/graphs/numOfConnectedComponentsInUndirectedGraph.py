def countComponents(n, edges):
  '''
  goal: return the number of connected components given edges
  n: int, edges: list[list[int]]
  return: int
  '''
  if not n:
    return 0

  # union find
  parent = [i for i in range(n)] # stores the parent for each node (initialized as i is a parent of itself)
  rank = [1]*n # stores the number of children node i has

  # finding root parent of node
  def find(node):
    res = node
    while res != parent[res]:
      parent[res] = parent[parent[res]]
      res = parent[res]
    return res

  # combines two nodes if they are supposed to be connected but not already stored
  def union(n1, n2):
    p1, p2 = find(n1), find(n2)
    if p1 == p2:
      return 0
    
    if rank[p1] > rank[p2]:
      parent[p2] = p1
      rank[p1] += rank[p1]
    else:
      parent[p1] = p2
      rank[p2] += rank[p1]
    return 1
  
  res = n
  for n1, n2 in edges:
    res -= union(n1,n2) # if union combines two components then the number of total components drops
  return res


  # dfs
  # set up adj list
  adj = {i: [] for i in range(n)}
  for i,j in edges:
    adj[i].append(j)
    adj[j].append(i)
  visited, path = set(), set()

  # dfs function
  def dfs(node, prev):
    if node in path:
      return False
    visited.add(node)
    path.add(node)
    for neighbor in adj[node]:
      if neighbor != prev:
        dfs(neighbor)
  
  count = 0
  for start in range(n):
    if start not in visited:
      path = set()
      count += 1
      dfs(start, -1)
  return count