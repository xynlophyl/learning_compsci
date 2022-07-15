def canFinish(numCourses, prerequisites):
  '''
  goal: given a number of courses (0-numCourses-1) and list of prerequisites for certain courses, return whether every course can be completed 
  numCourses: int, prerequisites: list[list[int]]
  return: bool
  '''
  adj = {i:[] for i in range(numCourses)}
  for p in prerequisites:
    adj[p[0]].append((p[1]))
  
  visited = set()
  def dfs(c):
    if c in visited:
      return False
    visited.add(c)
    for p in adj[c]:
      if not dfs(p):
        return False
    visited.remove(c)
    adj[c] = []
    return True
    
  for start in range(numCourses):
    if not dfs(start):
      return False
  return True
