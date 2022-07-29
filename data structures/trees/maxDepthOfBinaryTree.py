from trees import BinaryTreeNode

def maxDepth(root):
  '''
  goal: find the maximum depth/height of the given binary tree
  root: TreeNode or None
  return: int
  '''
  if not root:
    return 0
  return 1 + max(maxDepth(root.left), maxDepth(root.right))
  