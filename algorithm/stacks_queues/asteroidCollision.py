def asteroidCollision(asteroids):
  '''
  goal: given an array of asteroids (size, direction), return the asteroids that remian after collision
  asteroids: list[int]
  return: list[int]
  collision rules:
    for adjacent asteroids travelling in opposite directions, the larger asteroid destroys the smaller asteroid, 
    if they are the same size, then both are destroyed,
    repeat collisions until all asteroids are travelling in same direction, or there are no asteroids left
  '''
  stack = []
  for curr in asteroids:
    while stack and curr < 0 and stack[-1] > 0:
      if stack[-1] < curr*-1:
        stack.pop()
        continue
      elif stack[-1] == curr*-1:
        stack.pop()
      break
    else:
      stack.append(curr)
  return stack
