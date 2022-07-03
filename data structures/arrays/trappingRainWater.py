def trap(height):
  # multiple passes to record max heights in both directions: O(n) time, O(n) space
  right_max = height[0]
  right = []
  for i in height: #find the tallest block to the right of curr
    right_max = max(right_max,i)
    right.append(right_max)
  
  left_max = height[-1] #find the tallest block to the left of curr
  left = []
  for i in range(len(height),0,-1):
    left_max = max(left_max, height[i-1])
    left.append(left_max)
  left.reverse()
  
  res = 0
  for i in range(len(height)): #find the highest the water can fill up to at a certain column
    res += min(right[i],left[i])-height[i]
  
  return res