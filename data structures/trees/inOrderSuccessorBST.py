from trees import BinaryTreeNode as TreeNode

def inorderSuccessor(root, p):
  '''
  goal: return the next in order value of p in the given BST, root
  root: TreeNode, p: TreeNode
  return: TreeNode
  '''
  successor = None

  while root:
    if p.val >= root.val:
      root = root.right
    else:
      successor = root
      root = root.left
  return successor
        