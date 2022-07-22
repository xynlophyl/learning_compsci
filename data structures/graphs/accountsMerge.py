def accountsMerge(accounts):
  '''
  goal: merge accounts that contain the same email addresses
  accounts: list[list[str]]
  return: list[list[str]
  '''
  adj = {}
  emailToAcc = {}
  
  for acc in accounts:
    emailToAcc[acc[1]] = acc[0]
    for email in acc[2:]:
      if acc[1] in adj:
        adj[acc[1]].add(email)
      else:
        adj[acc[1]] = set([email])
      
      if email in adj:
        adj[email].add(acc[1])
      else:
        adj[email] = set([acc[1]])
  
  mergedAcc = []
  marked = set()
  for email in emailToAcc:
    if email in marked:
      continue
    
    group = []
    stack = [email]
    while stack:
      curr = stack.pop()
      if curr in marked:
        continue
      marked.add(curr)
      group.append(curr)

      for neighbor in adj.get(curr,set()):
        stack.append(neighbor)
    mergedAcc.append([emailToAcc[email]] + sorted(group))
  return mergedAcc
