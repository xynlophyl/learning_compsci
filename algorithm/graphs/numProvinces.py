def findCircleNum(isConnected):    
  '''
  goal: find the number of groups of circles given their connection status, isConnected
  isConnected: list[list[int]]
  return: int
  '''    
  
  n = len(isConnected[0])
  edges = []
  # set up
  for node, row in enumerate(isConnected):
    for neighbor, edge in enumerate(row):
      if node != neighbor and edge == 1:
        edges.append((node, neighbor))
  
  parent = [i for i in range(n)]
  rank = [1] * n
  
  # find parent
  def findParent(circle):
    curr = circle
    while curr != parent[curr]:
      parent[curr] = parent[parent[curr]]
      curr = parent[curr]
    return curr
  
  # combine nodes that are connected to a single parent/group
  def union(c1,c2):
    p1, p2 = findParent(c1), findParent(c2)
    if p1 == p2:
      return 0

    if rank[p1] > rank[p2]:
      parent[p2] = p1
      rank[p1] += rank[p2]
    else:
      parent[p1] = p2
      rank[p2] += rank[p1]
    return 1
  
  res = n
  for n1, n2 in edges:
    res -= union(n1,n2)
  return res