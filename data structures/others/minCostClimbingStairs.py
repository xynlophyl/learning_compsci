def minCostClimbingStairs(cost) -> int:
  '''
  goal: return the min cost to climb a set of stairs, given the cost of each step, and that you can take 1 or 2 steps at each iteration (you can also start at the first or second step)
  cost: list[int]
  returns: int
  '''

  # dynamic programming single pass: O(n) time, O(n) space
  if len(cost) == 2:
    return min(cost)
  
  opt = [-1] * len(cost)
  opt[-1] = cost[-1]
  opt[-2] = cost[-2]
  
  
  for i in range(len(cost)-3, -1, -1):
    opt[i] = min(opt[i+1], opt[i+2]) + cost[i]
  
  return min(opt[0], opt[1])