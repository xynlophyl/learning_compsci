class Node: # Definition for a Node.
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node):
  '''
  goal: create a soft copy of the given graph
  node: Node
  return: Node
  '''
  if not node:
    return None
  baseNode = Node()
  queue = [(node, baseNode)]
  visited = {}
  
  while queue:
    curr, copy = queue.pop(0)
    copy.val = curr.val
    for neighbor in curr.neighbors:
      if neighbor.val in visited:
        copyNeighbor = visited[neighbor.val]
      else:
        copyNeighbor = Node()
        visited[neighbor.val] = copyNeighbor
        queue.append((neighbor, copyNeighbor))
      copy.neighbors.append(copyNeighbor)
    visited[curr.val] = copy
  return baseNode