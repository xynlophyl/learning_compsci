def combinationSum(candidates, target):
  '''
  goal: return all lists of values from candidates (w/ repeating) where each list sums to target
  candidates: list[int], target: int
  return: list[list[int]] 
  '''
  # backtracking better solution, uses idea that lists are mutable through functions
  def optimizedReachedTarget(used, candidates,target, ret):
    if target < 0:
      return 
    if target == 0:
      ret.append(used)
      return
    for i in range(len(candidates)):
      optimizedReachedTarget(used + [candidates[i]], candidates[i:], target-candidates[i], ret)
  
  # backtracking
  def reachedTarget(used, candidates, target):
    if target < 0:
      return
    if target == 0:
      return used, True
    
    reached = []
    for i in range(len(candidates)):
      curr = reachedTarget(used+[candidates[i]], candidates[i:], target-candidates[i])
      if curr:
        if curr[1]:
          reached.append(curr[0])
        else:
          for i in curr[0]:
            reached.append(i)
    return reached, False
  
  ret = []
  optimizedReachedTarget([],candidates,target, ret)
  return ret
  
  ans = reachedTarget([], candidates, target)
  if ans:
    return ans[0]
  