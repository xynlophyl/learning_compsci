from trees import BinaryTreeNode as TreeNode

def lowestCommonAncestor(root,p, q):
  '''
  goal: find the lowest common ancestor of p and q in root (p and q are in the tree, all values of the tree are unique)
  root: TreeNode, p: TreeNode, q: TreeNode
  '''
  def dfs(node):
    if not node:
      return None
    
    if node == p or node == q:
      return node
    
    l, r = dfs(node.left), dfs(node.right)
    if l and r:
      return node
    
    return l if l else r
  
  return dfs(root)
    