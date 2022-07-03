def maxProfit(prices):      
  # save last min: O(n) time O(1) space
  last_min = prices[0]
  max_profit = 0
  
  for i in range(1,len(prices)):
    if prices[i] < last_min:
      last_min = prices[i]
    max_profit = max(max_profit, prices[i]-last_min)
  return max_profit
