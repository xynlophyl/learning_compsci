def coinChange(coins, amount):
  '''
  goal: given a list of different values of coins, check and find the minimum number of coins needed to reach amount
  '''
  opt = [float('inf')] *(amount+1) # optimal number of coints to get to its index
  opt[0] = 0 # 0 coins are needed to reach number 0
  
  for val in range(1, amount+1):
    for c in coins:
      if val-c >= 0:
        opt[val] = min(opt[val], opt[val-c] + 1)
  
  if opt[-1] == float('inf'):
    return -1
  return opt[-1]
