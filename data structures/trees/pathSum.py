from trees import BinaryTreeNode as TreeNode

# part I
def hasPathSum(root, targetSum):
  '''
  goal: check if there is a root-to-leaf path that sums to targetSum
  root: TreeNode or None, targetSum: int
  return: bool
  '''
  # dfs
  def dfs(node, target):
    if not node:
      return False
    
    target -= node.val
    if not node.left and not node.right:
      return target == 0
    return dfs(node.left, target) or dfs(node.right, target)
  
  return dfs(root, targetSum)

  # recursion 
  if not root:
    return False
  
  if not root.left and not root.right:
    return targetSum == root.val
  l = self.hasPathSum(root.left, targetSum - root.val) if root.left else False
  r = self.hasPathSum(root.right, targetSum - root.val) if root.right else False
  return l or r


# part II
def pathSum(root, targetSum):
  '''
  goal: return all root-to-leaf paths that sum to targetSum
  root: TreeNode or None, targetSum: int
  return: list[list[int]]
  '''
  if not root:
    return []
  
  paths = []
  def dfs(node, target, p):
    if not node:
      return False
    else: # theres a node
      new_p = p + [node.val]
      if not node.left and not node.right and target == node.val:
        paths.append(new_p)
      else:
        dfs(node.left, target-node.val, new_p)
        dfs(node.right, target-node.val, new_p)
  
  dfs(root, targetSum, [])
  return paths

# part III

def pathSum(root, targetSum):
  '''
  goal: return the number of subpaths of the given tree that sum to targetSum
  root: TreeNode or None, targetSum: int
  return: int
  '''
  if not root:
    return 0
  d = {0:1}
  
  def dfs(curr, ps):
    if not curr:
      return 0
    count = 0
    ps += curr.val
    
    if ps - targetSum in d:
      count += d[ps-targetSum]
    
    d[ps] = d.get(ps, 0) + 1
    count += dfs(curr.left, ps) + dfs(curr.right,ps)
    d[ps] -= 1
    return count
  
  return dfs(root, 0)
      