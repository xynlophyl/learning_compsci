def valid_tree(n, edges):
  '''
  goal: check if edges given represent a valid tree with n nodes
  n: int, edges: list[list[int]]
  return: bool
  '''
  if not n:
    return False

  adj = {i: [] for i in range(n)}
  for node, neighbor in edges:
    adj[node].append(neighbor)
    adj[neighbor].append(node)
    
  visited = set()
  
  def dfs(node, prev):
    if node in visited:
      return False
        
    visited.add(node)
    for neighbor in adj[node]:
      if neighbor == prev:
        continue
      if not dfs(neighbor, node):
          return False
    return True
    
  return dfs(0,-1) and len(visited) == n
