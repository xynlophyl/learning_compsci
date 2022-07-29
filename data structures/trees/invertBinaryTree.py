from trees import BinaryTreeNode as TreeNode

def invertTree(root):
  '''
  goal: invert binary tree
  root: TreeNode or None
  return: TreeNode or None
  '''
  if not root:
    return None
  
  root.left, root.right = invertTree(root.right), invertTree(root.left)
  return root