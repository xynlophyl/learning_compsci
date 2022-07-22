# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowestCommonAncestor(root, p, q):
  '''
  goal: find the lowest common ancestor of p and q
  root: TreeNode, p: TreeNode, q: TreeNode
  return: TreeNode 
  '''
  if not root:
    return None
  l, h= min(p.val, q.val), max(p.val, q.val)
  def search(root):
    if not root:
      return None
    if root.val == l or root.val == h or (root.val > l and root.val < h):
      return root
    elif root.val > l and root.val > h:
      return search(root.left)
    else:
      return search(root.right)
    
  return search(root)