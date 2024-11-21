from ..implementations.trees import BinaryTreeNode as TreeNode

def isSameTree(p,q):
  '''
  goal: check if p and q are the trees with identical structure and values
  p: TreeNode or None, q: TreeNode or None
  return: bool
  '''
  if not p and not q:
    return True
  elif (p and not q) or (not p and q) or (p.val != q.val):
    return False
  else:
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
