from trees import BinaryTreeNode as TreeNode
def maxPathSum(root):
  '''
  goal: find a subpath of the given tree that returns the max sum
  root: TreeNode or None
  return: int
  '''
  if not root:
    return 0
  
  ret = [root.val]
  def get_max_dfs(curr):
    if not curr:
      return 0
    
    l = max(0, get_max_dfs(curr.left))
    r = max(0, get_max_dfs(curr.right))
    
    ret[0] = max(ret[0], curr.val+l+r)
    
    return curr.val + max(l, r)
    
  
  get_max_dfs(root)
  return ret[0]
