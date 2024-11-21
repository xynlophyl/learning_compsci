# Part I
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

# Part II
def findOrder(numCourses, prerequisites):
  '''
  goal: given prerequisites for a number of courses, if you are able to finish all courses (w/o any conflicts) return the order you need to complete them in, else return []
  numCourses: int, prerequisites: list[list[int]]
  return: list[int]
  '''
  # creating adjacency list
  adj = {i: [] for i in range(numCourses)}
  for course, prereq in prerequisites:
    adj[course].append(prereq)
  
  visited, path = set(), set()
  order = []
  
  # defining dfs 
  def dfs(course):
    if course in path:
      return False
    if course in visited:
      return True
    
    path.add(course)
    for next_course in adj[course]:
      if not dfs(next_course):
        return False
      
    path.remove(course)
    visited.add(course)
    order.append(course)
    return True
    
  # running on every course
  for start in range(numCourses):
    if not dfs(start):
      return []
    
  return order
