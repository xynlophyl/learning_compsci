def canCompleteCircuit(gas, cost):
  '''
  goal: given available gas at and cost to reach a station return which station to start at to complete a journey in order
  gas: list[int], cost: list[int]
  return: int
  '''
  # greedy: O(n) time, O(1) space
  if sum(gas) < sum(cost): # O(1) or O(n) depending on if sum is saved as a prop in list
    return -1
  
  res = 0
  tank = 0
  for i in range(len(gas)): # O(n)
    tank += gas[i] - cost[i]
    if tank < 0:
      tank = 0
      res = i + 1
  return res
